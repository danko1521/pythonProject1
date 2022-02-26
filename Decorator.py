import functools
from datetime import datetime
import logging

nested_list = [
    ['a', 'b', False, 'c', 'gig', [12, 13]],
    ['d', 'e', 'f', 'h', False],
    ['p', 'i', 'g', 'g'],
    [1, 2, 3, 4, 5]
]


def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"вызывается функция {func.__name__} с аргументом({signature})")
        value = func(*args, **kwargs)
        print(f"функция {func.__name__!r} вернула аргумент {value!r}")
        now = datetime.now()
        current_time = now.strftime("%y:%m:%d:%H:%M:%S")
        with open("loger.txt", "w") as file:
            file.write(f'time calling function {current_time}, name func {func.__name__},'
                       f' func return argument {signature} and return value {value}')
        return value

    return wrapper_debug


@debug
def some_list_of_list(nested_list):
    for some_list in nested_list:
        for elem in some_list:
            if bool(elem) in some_list:
                elem = str(elem)
            for el in elem:
                yield el
    flattened = [elem for list in nested_list for elem in list]
    print(flattened)


for item in some_list_of_list(nested_list):
    print(item)
