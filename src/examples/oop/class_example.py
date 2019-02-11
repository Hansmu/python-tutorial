from .inheritance import inheritance_example
from .special_methods import special_methods_example


class Example:
    is_testing = True

    # constructor, self keyword refers to the object itself
    def __init__(self, example_type):
        self.example_type = example_type

    def bark(self):
        print('Woof ' + self.example_type)


def class_example():
    example = Example('Some example')
    example.bark()

    inheritance_example()
    special_methods_example()
