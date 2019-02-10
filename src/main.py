x = 50
print('Hello world')


def reassign_global():
    global x
    x = 200


reassign_global()
print(x)

