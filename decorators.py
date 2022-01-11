from functools import wraps


# outer function
def decorators(xyz):
    @wraps(xyz)
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        print(args[0]+args[1])
        data = xyz(*args, **kwargs)
        print(data)
        print(args[2]-kwargs.get('d'))

    return wrapper


@decorators
def add(a, b, c, d):
    return a-b+c+d


add(10, 20, 30, d=40)



