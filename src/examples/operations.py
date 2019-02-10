from random import shuffle
from random import randint


def operation_examples():
    comparison_examples()
    if_else_examples()
    loops_examples()
    useful_operators()


def comparison_examples():
    print(2 > 1)
    print(1 < 2)
    print(2 >= 2)
    print(2 <= 2)
    print(2 <= 3 and 5 < 6 or 1 == 2)
    print(not 2 > 3)
    print(2 == 2)
    print(2 != 3)


def if_else_examples():
    some_condition = True

    if some_condition:
        print('Yup, true')
    elif not some_condition:
        print('Else if')
    else:
        print('Not gonna reach here with those conditions')


def loops_examples():
    some_list = [1, 2, 3]

    # If the list items aren't used, then _ is often used as the item name
    for item in some_list:
        print(item)

    another_list = [(1, 2), (3, 4), (5, 6)]

    # Can add more variables to unpack longer tuples
    for first_tuple_element, second_tuple_element in another_list:
        print(first_tuple_element, second_tuple_element)

    dictionary = {'k1': 1, 'k2': 2}

    for key, value in dictionary.items():
        print(key, value)

    x = 0

    while x < 3:
        # break jumps out of the loop, continue goes to the top ignoring the rest of the body
        print('Still not 3')
        x += 1
    else:
        print('Finally 3')


def useful_operators():
    even_numbers = list(range(0, 10, 2))

    for num in range(0, 10, 2):
        print(num)

    word = 'abcde'

    # Enumerate returns info on the specific list element as a tuple
    for index, letter in enumerate(word):
        print(index, letter)

    one_list = [1, 2, 3]
    two_list = ['a', 'b', 'c']

    # Zip creates tuples of however many lists there are
    # Zip ignores extra, if one list is longer than another
    for item in zip(one_list, two_list):
        print(item)

    # Check if something is in a list
    print('x' in [1, 2, 3])
    print(2 in [1, 2, 3])
    print('mykey' in {'mykey': 345})

    print(min(one_list))
    print(max(one_list))

    my_list = [1, 2, 54, 1, 2, 3]
    shuffle(my_list)
    random_number = randint(0, 100)

    user_value = input('Enter a number here: ')
