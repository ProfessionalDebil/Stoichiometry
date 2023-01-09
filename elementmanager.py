import json

from element import *
from molecule import *
from errorhandling import ElementNotDefined

class ElementManager:
    """
    This is the class that manages references to the elements

    Attributes:

    Methods:
        add_element(element: dict) -> None:
                Returns the mass of the molecule
    """

    def __init__(self) -> None:
        self.element_count: int = 118
        self.elements: list[Element] = [None for _ in range(self.element_count)]
        self.element_index: dict[str, int] = {}
        
        with open("ElementData.json") as element_file:
            element_data = json.load(element_file)
            
            for element in element_data:
                self.add_element(element)

    def add_element(self, element: dict[str, int | str | float]) -> None:
        """
        This method is to add elements to the element manager

        Parameters:
            element: dict[str, int | str | float]

        Returns:
            None
        """

        # the self.elements work by indexing atom number - 1

        number = element['number']
        index = number - 1
        symbol = element['symbol']
        element = Element(number,
                          element['name'],
                          symbol,
                          element['mass'],
        )

        self.elements[index] = element
        self.element_index[symbol] = index

    def get(self, target: int | str) -> Element:
        """
        Get an element from the element manager with the atomic number or the element symbol

        Parameters:
            target: int | str

        Returns:
            Element
                The element that is fetched

        Raises:
            ElementNotDefined
                If the element is not defined on self.elements
        """

        if isinstance(target, int): # if user supplies atomic number
            try:
                return self.elements[target - 1]
            except IndexError:
                raise ElementNotDefined

        elif isinstance(target, str): # if user supplies element symbol
            try:
                return self.elements[self.element_index[target]]
            except KeyError:
                raise ElementNotDefined

        raise ElementNotDefined

    #def formula_to_molecule(self, formula: str) -> Molecule:
    #    isNum = False

    #    for letter in formula:
    #        