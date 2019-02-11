def new_decorator(original_func):
    def wrap_func():
        print('Extra code')
        original_func()
        print('Extra after')

    return wrap_func


#  Same as new_decorator(func_needs_decorator)
@new_decorator
def func_needs_decorator():
    print('Decorate me')


func_needs_decorator()
