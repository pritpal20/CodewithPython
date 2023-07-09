from common.helper_functions import create_array


def print_args(func):

    def inner_func(*args,**kwargs):

        ret = func(*args,**kwargs)
        return ret 

    return inner_func

@print_args
def func(*args,**kwargs):
    print("args ", args)
    arr = []
    for a in args:
        arr = []
        arr = create_array(a)

        arr.sort()
    return arr


arr = func(10)
print(arr)

