def data_types_examples():
    numbers_and_maths_examples()
    string_examples()
    lists_examples()
    dictionary_examples()
    tuple_examples()
    sets_examples()
    boolean_examples()


def numbers_and_maths_examples():
    number = 187213
    floating_point = 3.1241124

    adding = 2 + 1
    subtraction = 4 - 1
    multiplication = 2 * 3
    division = 5 / 2
    modulus = 7 % 4
    power_to = 2 ** 4

    print('-----------------NUMBERS EXAMPLES HERE--------------------')
    print(number, floating_point, adding, subtraction, multiplication, division, modulus, power_to)
    print(type(number), type(floating_point))


def string_examples():
    string = 'Hello'
    also_string = "Hello \nfriend"
    nested = "Oh no, don't do that!"

    print('--------------STRING EXAMPLES HERE------------------')
    print(string, also_string, nested)
    print('Grab from the start: ', string[0], string[1])
    print('Grab from the end: ', string[-1], string[-2])
    print('Get the string length: ', len(also_string))
    print('From index to end: ', also_string[2:])
    print('Get up until index: ', nested[:3])
    print('String section: ', nested[2:6])
    print('Specify step size: ', nested[::2], nested[2:7:2])
    print('Reverse string: ', string[::-1])
    print('Concat: ', string + ' ' + also_string)
    print('Spam letters: ', 'z' * 10)
    print('Some methods', string.upper(), string.lower(), nested.split(', '))

    print('String here {}, then also {}'.format('yup', 'here too'))
    print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
    print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))
    print('The result was formatted to 3 float points {r:1.3f}'.format(r=100/77))
    print('The result was formatted to 5 float points {r:1.5f}'.format(r=100/77))

    # f-string
    print(f'Also interpolation for {100/77}')


def lists_examples():
    some_list = [1, 2, 3]
    other_list = ['String', 100, 23.2]
    print(len(other_list), other_list[0])
    print('Some operations for reading indexes: ', other_list[1:])
    print('Concat lists', some_list + other_list)
    other_list.append('New element')
    other_list.pop()
    # Reverse indexing works as well
    other_list.pop(0)
    num_list = [4, 1, 9, 2, 4]
    num_list.sort()
    num_list.reverse()
    print([1] * 3)


def dictionary_examples():
    some_dict = {'key1': 'value1', 'key2': 100.2}
    print(some_dict['key1'])
    print(some_dict.items())
    print(some_dict.keys())
    print(some_dict.values())


def tuple_examples():
    some_tuple = (1, 2, 3, 'a', 'b', 'c', 'a')
    print(some_tuple.count('a'))
    print(some_tuple[-1])


def sets_examples():
    some_list = [1, 1, 2, 2, 3, 4, 3]
    some_set = set()
    some_set.add('abc')
    some_set.add('abc')
    print(set(some_list))


def boolean_examples():
    some_bool = False
    placeholder = None
    print(placeholder, some_bool, 1 > 2, 2 < 1)
