from rdkit import Chem
from rdkit.Chem import AllChem


class AtomList:
    _symbols: list[str]
    _geometry: list[list[float]]

    def __init__(self, symbols: list[str], geometry: list[list[float]]):
        self._symbols = symbols
        self._geometry = geometry

    def from_smiles(smiles: str):
        mol = Chem.MolFromSmiles(smiles)
        mol = Chem.AddHs(mol, explicitOnly=False)
        AllChem.EmbedMolecule(mol)

        symbols = []
        geometry = []

        for i, atom in enumerate(mol.GetAtoms()):
            positions = mol.GetConformer().GetAtomPosition(i)
            symbols.append(atom.GetSymbol())
            geometry.append(positions.x)
            geometry.append(positions.y)
            geometry.append(positions.z)

        return AtomList(symbols, geometry)

    def __str__(self):
        atomlist = ""

        for i, atom in enumerate(self._symbols):
            coords = self._geometry[3 * i : 3 + 3 * i]
            atomlist += f"{atom} {str(coords)[1:-1].replace(",", "")};"

        return atomlist
