def operation_examples():
    comparison_examples()
    if_else_examples()


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
