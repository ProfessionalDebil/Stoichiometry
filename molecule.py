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

    def __init__(self, elements: dict["Element", int]):
        self.elements = elements
        self.mass = self.calculate_mass()

    def calculate_mass(self) -> float:
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

            result_mass = mass * quantity

        return result_mass