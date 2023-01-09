from element import *

class Molecule:
    """
    This is the class for Molecules such as CO2, H20, and NH3

    Attributes:
        elements : dict[Element, int]
            The components of the molecule

    Methods:
        calculate_mass() -> float:
            Returns the mass of the molecule
    """

    def __init__(self, elements: dict["Element", int]) -> None:
        self.elements = elements
        self.molar_mass = self.calculate_mass(1)
        self.element_percentage = self.calculate_element_percentage()

    def calculate_element_percentage(self) -> list(float):
        """
        Calculate the percentage of the component element in the molecule

        Returns:
            list[float]
                List of element percentage in the molecule. Sum of this list equals 1
        """

        result = []

        for pair in self.elements.items():
            element: Element = pair[0]
            quantity = pair[1]

            element_mass = element.mass * quantity
            
            result.append(element_mass / self.molar_mass)

        return result

    def calculate_mass(self, mol: float) -> float:
        """
        Calculate the atomic mass of the molecule

        Returns:
            float
                The atomic mass of the molecule
        """

        result_mass = 0

        for pair in self.elements.items():
            mass = pair[0].mass
            quantity = pair[1]

            result_mass += mass * quantity

        return result_mass / mol

    def calculate_mol(self, a: float) -> float:
        """
        Calculate the mol of the molecule using the formula n = a / M

        Parameters:
            a: float
                Substance mass in gram

        Returns:
            float
        """

        return a / self.molar_mass

    def calculate_volume(self, n: float, temp: float = 273.15, pressure: float = 1) -> float:
        """
        Calculate the volume of a gas using the formula v = n r T / P

        Parameters:
            a: float
                Substance mass

            temp: float = 273.15
                Temperate in Kelvin

            pressure: float = 1
                Pressure in atm

        Returns:
            float
        """

        r = 0.082 # ideal gas constant
        factor = 22.3983

        if temp != 273.15 or pressure != 1:
            factor = temp * r / pressure

        return n * factor

    def calculate_pressure(self, n: float, temp: float = 273.15, volume: float = 1) -> float:
        """
        Calculate the pressure of a gas using the formula P = n r T / v

        Parameters:
            a: float
                Substance mass

            temp: float = 273.15
                Temperate in Kelvin

            volume: float = 1
                volume in litre

        Returns:
            float
        """

        r = 0.082 # ideal gas constant
        factor = 22.3983

        if temp != 273.15 or volume != 1:
            factor = temp * r / volume

        return n * factor

    def add_molecule(self, molecule: "Molecule") -> "Molecule":
        """
        Combine two molecules to make a new one, example combine H2 with SO4 to make H2SO4

        Parameters:
            a: float
                Substance mass

        Returns:
            float
        """

        if not isinstance(molecule, Molecule):
            return TypeError(f"Cannot add object of type {type(molecule).__name__}")

        new_elements = self.elements.copy()

        for pair in molecule.elements.items():
            element = pair[0]
            quantity = pair[1]

            try:
                new_elements[element] += quantity
            except KeyError:
                new_elements[element] = quantity

        return Molecule(new_elements)