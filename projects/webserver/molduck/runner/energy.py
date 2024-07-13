from pyscf import dft, gto, scf
from pyscf.lib.exceptions import BasisNotFoundError

from molduck.utils.atom_list import AtomList
from molduck.utils.error import error
from molduck.schemas import QCSchemaInput


def energy(calc: QCSchemaInput):
    is_dft = False

    try:
        if calc.model.method in ["HF", "RHF", "UHF"]:
            method = getattr(scf, calc.model.method)
        else:
            is_dft = True
            method = getattr(dft, calc.model.method)
    except AttributeError:
        return error(
            "",
            f"Method '{calc.model.method}' not found.",
        )

    atomlist = AtomList(calc.molecule.symbols, calc.molecule.geometry)

    try:
        mol = gto.M(
            atom=str(atomlist),
            basis=calc.model.basis,
        )
    except BasisNotFoundError:
        return error(
            "",
            f"Basis set '{calc.model.basis}' not found",
        )

    mf = method(mol)

    if is_dft:
        if calc.keywords and calc.keywords.xc:
            mf.xc = calc.keywords.xc

    mf.verbose = False

    try:
        mf.run()
    except KeyError as err:
        return error("key_error", str(err))

    return {
        "success": True,
        "properties": {
            "calcinfo_nbasis": mf.mol.nbas,
            "calcinfo_nmo": len(mf.mo_occ),
            "calcinfo_natom": mf.mol.natm,
            "calcinfo_nalpha": mf.mol.nelec[0],
            "calcinfo_nbeta": mf.mol.nelec[1],
            "return_energy": mf.energy_tot(),
            "scf_one_electron_energy": mf.energy_elec()[0],
            "scf_two_electron_energy": mf.energy_elec()[1],
            "scf_total_energy": mf.energy_tot(),
            "nuclear_repulsion_energy": mf.energy_nuc(),
        },
    }
