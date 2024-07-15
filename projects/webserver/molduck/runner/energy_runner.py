from typing import Any

from pyscf import dft, scf

from molduck.runner.error import Error, ErrorType
from molduck.runner.runner import Runner


HF_METHODS = (
    "HF",
    "RHF",
    "UHF",
)

POST_HF_METHODS = ("MP2",)

KS_METHODS = (
    "KS",
    "RKS",
    "UKS",
)


class EnergyRunner(Runner):
    _callback_function: Any = None
    _method_function: Any
    _mf: Any

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.had_error:
            return

        self._method()

    def _method(self):
        if self.input_data.model.method.upper() in HF_METHODS:
            self._method_function = self._hartree_fock
        elif self.input_data.model.method.upper() in KS_METHODS:
            self._method_function = self._kohn_sham
        else:
            match self.input_data.model.method.upper():
                case "MP2":
                    self._method_function = self._moller_plesset_2
                case _:
                    self.error = Error(ErrorType.METHOD_NOT_FOUND, "Invalid method.")
                    return

        self._method_function()

    def run(self):
        if self.had_error:
            print(self.error)
            print(self._error)
            return {"success": False} | self.error

        try:
            self._mf.run()
        except KeyError as err:
            self.error = Error(
                ErrorType.KEYWORD_NOT_FOUND,
                str(err),
            )

        if self.had_error:
            return {"success": False} | self.error

        output_data = (
            {} if self._callback_function is None else self._callback_function()
        )

        return {
            "success": True,
            "return_result": output_data.get("return_energy"),
            "properties": self._calc_info() | output_data,
        }

    def _calc_info(self):
        return {
            "calcinfo_nbasis": self._mf.mol.nbas,
            "calcinfo_nmo": len(self._mf.mo_occ),
            "calcinfo_natom": self._mf.mol.natm,
            "calcinfo_nalpha": self._mf.mol.nelec[0],
            "calcinfo_nbeta": self._mf.mol.nelec[1],
        }

    def _hartree_fock(self, method: str | None = None):
        method = getattr(scf, method or self.input_data.model.method)
        self._mf = method(self.mol)
        self._mf.verbose = False
        self._callback_function = self._hf_ks_callback

    def _hf_ks_callback(self):
        return {
            "return_energy": self._mf.energy_tot(),
            "scf_one_electron_energy": self._mf.energy_elec()[0],
            "scf_two_electron_energy": self._mf.energy_elec()[1],
            "nuclear_repulsion_energy": self._mf.energy_nuc(),
            "scf_dipole_moment": self._mf.dip_moment().tolist(),
            # "scf_iterations": 1,
            "scf_total_energy": self._mf.energy_tot(),
        }

    def _kohn_sham(self):
        method = getattr(dft, self.input_data.model.method)
        self._mf = method(self.mol)
        self._mf.verbose = False

        if self.input_data.keywords and self.input_data.keywords.xc:
            self._mf.xc = self.input_data.keywords.xc

        self._callback_function = self._hf_ks_callback

    def _moller_plesset_2(self):
        self._hartree_fock("HF")

        try:
            self._mf.run()
        except KeyError as err:
            return self._error(ErrorType.KEYWORD_NOT_FOUND, str(err))

        self._mf = self._mf.MP2()
        self._callback_function = self._moller_plesset_2_callback

    def _moller_plesset_2_callback(self):
        return {
            "return_energy": self._mf.e_tot,
            "scf_one_electron_energy": self._mf._scf.scf_summary.get("e1"),
            "scf_two_electron_energy": self._mf._scf.scf_summary.get("e2"),
            "nuclear_repulsion_energy": self._mf._scf.scf_summary.get("nuc"),
            "scf_total_energy": self._mf.e_hf,
            "mp2_correlation_energy": self._mf.e_corr,
            "mp2_total_energy": self._mf.e_tot,
        }
