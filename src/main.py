from examples import data_types
from examples.oop import class_example

x = 50


data_types.data_types_examples()
class_example.class_example()


def reassign_global():
    global x
    x = 200


reassign_global()
print(x)

