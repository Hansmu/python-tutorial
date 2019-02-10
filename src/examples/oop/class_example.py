class Example:
    is_testing = True

    # constructor, self keyword refers to the object itself
    def __init__(self, example_type):
        self.example_type = example_type

    def bark(self):
        print('Woof ' + self.example_type)


example = Example('Some example')
example.bark()
