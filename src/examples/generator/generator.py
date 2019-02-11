# Don't have to hold everything in memory, just generates as needed
def create_cubes(n):
    for x in range(n):
        yield x**3


my_list = list(create_cubes(4))
cube_generator = create_cubes(4);

print(next(cube_generator))
print(next(cube_generator))
print(next(cube_generator))

s_iter = iter('Bob')
print(next(s_iter))
print(next(s_iter))
