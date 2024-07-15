from abc import ABC, abstractmethod

from pyscf import gto
from pyscf.gto import Mole
from pyscf.lib.exceptions import BasisNotFoundError

from molduck.schemas import QCSchemaInput
from molduck.utils.atom_list import AtomList
from molduck.runner.error import Error, ErrorType


class Runner(ABC):
    input_data: QCSchemaInput
    mol: Mole
    had_error: bool = False
    _error: Error | None = None

    def __init__(self, input_data: QCSchemaInput):
        self.input_data = input_data

        self._create_mol()

    def _create_mol(self):
        try:
            self.mol = gto.M(
                atom=str(
                    AtomList(
                        self.input_data.molecule.symbols,
                        self.input_data.molecule.geometry,
                    )
                ),
                basis=self.input_data.model.basis,
            )
        except BasisNotFoundError:
            self.error = Error(
                ErrorType.BASIS_NOT_FOUND,
                "Invalid basis set.",
            )

    @property
    def error(self):
        if self.had_error:
            return {
                "error": {
                    "error_type": self._error.error_type.value,
                    "error_message": self._error.error_message,
                },
            }

    @error.setter
    def error(self, error: Error):
        self.had_error = True
        self._error = error

    @abstractmethod
    def run(self):
        pass
