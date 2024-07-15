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


class Error(Schema):
    error_type: str
    error_message: str


class QCSchemaProperties(Schema):
    calcinfo_nbasis: int
    calcinfo_nmo: int
    calcinfo_nalpha: int
    calcinfo_nbeta: int
    calcinfo_natom: int
    return_energy: Optional[float] = None
    scf_one_electron_energy: Optional[float] = None
    scf_two_electron_energy: Optional[float] = None
    nuclear_repulsion_energy: Optional[float] = None
    scf_dipole_moment: Optional[list[float]] = None
    scf_iterations: Optional[int] = None
    scf_total_energy: Optional[float] = None
    mp2_correlation_energy: Optional[float] = None
    mp2_total_energy: Optional[float] = None
    cisd_correlation_energy: Optional[float] = None
    cisd_total_energy: Optional[float] = None
    fci_correlation_energy: Optional[float] = None
    fci_total_energy: Optional[float] = None


class QCSchemaInput(Schema):
    molecule: Molecule
    model: Model
    driver: str
    keywords: Optional[Keywords] = None


class QCSchemaOutput(Schema):
    return_result: Optional[Any] = None
    success: bool
    error: Optional[Error] = None
    properties: Optional[QCSchemaProperties] = None


class Job(Schema):
    uuid: UUID
    status: int
    input_data: QCSchemaInput
    output_data: Optional[QCSchemaOutput] = None
