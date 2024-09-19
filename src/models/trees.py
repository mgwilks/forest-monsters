from enum import Enum

class TreeType(Enum):
    """Enum class to declare different types of trees. """
    DECIDUOUS = "Deciduous"
    CONIFEROUS = "Coniferous"
    EVERGREEN = "Evergreen"
    PALM = "Palm"
    FRUIT = "Fruit"
    BROADLEAF = "Broadleaf"

class Tree:
    """Model class for a Tree"""

    height: float
    name: str
    diameter: float
    type: TreeType

    def __init__(self, height: float, name: str, type: TreeType) -> None:
        self.height = height
        self.name = name
        self.type = type

        print(f"Hello! My name is {self.name} and I am a {self.type.name} tree!")

    def shapeshift(self, desired_tree_type: TreeType) -> None:
        """This method lets a tree change into a different type!"""

        if desired_tree_type == self.type:
            print("The tree is already that type, silly.")
            return

        print("OOOOOOOO SOMETHING IS HAPPENING!!! Arghhghghghh!")
        self.type = desired_tree_type
        print(f"Woohoo! I've changed to a {self.type.name} tree!")
