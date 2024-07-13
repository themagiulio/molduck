from uuid import UUID
from typing import Any, Optional

from ninja import Schema


class Molecule(Schema):
    molecular_charge: Optional[int] = None
    molecular_multiplicity: Optional[int] = None
    geometry: list[float]
    symbols: list[str]


class Model(Schema):
    method: str
    basis: str | dict[str, str]


class Keywords(Schema):
    xc: Optional[str] = None


class QCSchemaProperties(Schema):
    calcinfo_nbasis: int
    calcinfo_nmo: int
    calcinfo_nalpha: int
    calcinfo_nbeta: int
    calcinfo_natom: int
    return_energy: float
    scf_one_electron_energy: float
    scf_two_electron_energy: float
    nuclear_repulsion_energy: float
    scf_dipole_moment: list[float]
    scf_iterations: int
    scf_total_energy: float


class QCSchemaInput(Schema):
    molecule: Molecule
    model: Model
    driver: str
    keywords: Optional[Keywords] = None


class QCSchemaOutput(QCSchemaInput):
    return_result: Optional[Any] | None
    success: bool
    properties: QCSchemaProperties


class Job(Schema):
    uuid: UUID
    success: bool
    input_data: QCSchemaInput
    output_data: Optional[Any]
