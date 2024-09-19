from enum import Enum, auto

class PlantType(Enum):
    TREE = auto()
    SHRUB = auto()
    HERB = auto()
    GRASS = auto()
    FERN = auto()
    VINE = auto()
    SUCCULENT = auto()
    CACTUS = auto()
    AQUATIC = auto()
    MOSS = auto()
    ORCHID = auto()
    BAMBOO = auto()
    PALM = auto()
    CONIFER = auto()
    FLOWERING = auto()

class Plant:
    """This is my friendly plant class!"""

    name: str
    height: float
    number_of_leaves: int
    number_of_branches: int
    type: PlantType

    def __init__(self, name: str, height: float, number_of_leaves: int, number_of_branches: int, type: PlantType) -> None:

        self.name = name
        self.height = height
        self.number_of_leaves = number_of_leaves
        self.number_of_branches = number_of_branches
        self.type = type

        print(f"Hi! My name is {self.name} and I am a {self.type.name} plant!")

    def add_number_of_leaves_and_branches(self) -> int:
        """This method is used to add the total number of leaves and branches together"""

        print(f"Adding together {self.number_of_leaves} and {self.number_of_branches}:")

        total = self.number_of_leaves * self.number_of_branches

        print(f"--> The total is {total}!")

        return total
