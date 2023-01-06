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
    
    def __init__(self, number: int, name: str, symbol: str, mass: float):
        self.number = number
        self.name = name
        self.symbol = symbol
        self.mass = mass