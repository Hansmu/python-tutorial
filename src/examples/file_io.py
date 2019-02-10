def file_io():
    # Or full path to the file
    some_file = open('text.txt')
    # Read goes to the end of the file
    print(some_file.read())
    # Moves the read cursor back to the start
    some_file.seek(0)
    print('Get an array for each line: ', some_file.readlines())

    some_file.close()


with open('text.txt') as my_file:
    # Automatically closes file
    contents = my_file.read()
    print(contents)


# w overwrites existing file. W is for write, a is for append
with open('text.txt', mode='a') as my_file_2:
    my_file_2.write('Bananas')
