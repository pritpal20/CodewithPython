from random import randint

def create_array(n : int ):

    if n <= 0 :
        raise ValueError(f"invalid argument {n}")
    arr = []
    for i in range(-n,n):
        while True:
            num = randint(-n,n-1)
            if num not in arr:
                arr.append(num)
                break

    return arr

def create_array_unsigned(n : int ):
    
    if n <= 0 :
        raise ValueError(f"invalid argument {n}")
    arr = []
    for i in range(n):
        while True:
            num = randint(0,n-1)
            if num not in arr:
                arr.append(num)
                break

    return arr