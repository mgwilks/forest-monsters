# This is a simple script that loads a Tree class from src/models/tree and executes some of the methods!


from models.trees import Tree, TreeType
from models.plants import Plant, PlantType


if __name__ == "__main__":

    # create instance of tree class
    tree = Tree(name="Sebastian", height=40.2, type=TreeType.EVERGREEN)


    # execute tree class' .shapeshift() method to transform into a new tree!
    tree.shapeshift(desired_tree_type=TreeType.PALM)


    # create instance of plant class
    plant = Plant(
        name="Timothy",
        height=120,
        number_of_leaves=100,
        number_of_branches=25,
        type = PlantType.CACTUS
    )

    # execute plants class method to add together number of leaves and branches
    total = plant.add_number_of_leaves_and_branches()
