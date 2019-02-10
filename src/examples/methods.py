def method_example():
    '''
    DOCSTRING: Information about the method is added here.
    INPUT: information about the input variables
    OUTPUT: information about the output
    '''

    name_method_example('Sally')
    name_method_example()


def name_method_example(name='Bobbert'):
    print('Hello ' + name)
    return name


# *args puts it into a tuple. Args is not needed, a random word can be there.
# **kwargs takes it in as a dictionary. my_func(fruit='apple', veggie='lettuce'). Can use both in the signature as well
# myFunc(10, 20, 30, fruit='orange', food='eggs', animal='dog')
def arbitrary_number_of_inputs_example(*args):
    print(sum(args) * 0.05)


def lambda_examples():
    my_nums = [1, 2, 3, 4, 5]
    # Or provide a function in place as a reference
    squared_nums = list(map(lambda x: x**2, my_nums))
    even_squared = list(filter(lambda num: num % 2 == 0, squared_nums))
    print(squared_nums)
    print(even_squared)

