""" Shortened periodic table data"""

class element():
    """
    Class representing an element with information on the symbol,name,
    atomic number and relative atomic mass

    Attributes
    ----------
    symbol : String
        Atomic symbol is passed to the class
    name: String
        Element name
    mass: float
        Relative atomic mass associated with the passed symbol
    number: integer
        Atomic number associated with the passed symbol
    """

    def __init__(self,symbol):
        names={"H": "Hydrogen","Boron":"B","C":"Carbon","N":"Nitrogen","O":"Oxygen",
        "F":"Fluorine","Si":"Silicon","P":"Phosphorus","S":"Sulfur","Cl":"Chlorine",
              "Bromine":"Br","I":"Iodine"}
        masses={"H": 1.007825, "B":10.81,"C": 12.011, "N":14.007, "Oxygen":15.999,
               "F":18.998,"Si":28.0855,"P":30.9738,"S":32.06,"Cl":35.453,"Br":79.904,
               "I":126.909}
        numbers={"H": 1, "Boron":5, "C": 6, "N": 7, "O": 8, "F":9,"Si":14,"P":15,"S":16,
                "Cl":17,"Br":35,"I":53}
        self.symbol = symbol
        self.name = names[symbol]
        self.mass = masses[symbol]
        self.atomic = numbers[symbol]
