def operation_examples():
    comparison_examples()
    if_else_examples()
    loops_examples()


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