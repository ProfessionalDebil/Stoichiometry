from molecule import *

class Element:
    """
    This is the class for Elements such as H, Fe, and O

    Attributes:
        number : int
            The atomic number of the element
        name : str
            The full name of the element
        symbol : str
            The symbol of the element
        mass : float
            The atomic mass of the element

    Methods:
    """
    
    def __init__(self, number: int, name: str, symbol: str, mass: float) -> None:
        self.number = number
        self.name = name
        self.symbol = symbol
        self.mass = mass

    def __eq__(self, other):
        if not isinstance(other, Element):
            return TypeError(f"Object of type {type(other).__name__} is not an Element")

        return self.number == other.number

    def __hash__(self):
        return hash((self.number, self.symbol))

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return self.symbol

    def __add__(self, other: "Element") -> "Molecule":
        """
        Return a molecule consisting of this element and the other element. Both Element are 1 in quantity

        Returns:
            Molecule
                The molecule that is made with both element
        """

        return Molecule({self: 1, other: 1})