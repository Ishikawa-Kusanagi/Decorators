# import datetime
# from functools import wraps
#
#
# def my_func(old_function):
#     @wraps(old_function)
#     def new_function(*args, **kwargs):
#         start = datetime.datetime.now()
#         print(f'Name func: {old_function.__name__}')
#         result = old_function(*args, **kwargs)
#         print(f'time to delay: {datetime.datetime.now() - start}')
#
#         return result
#
#     return new_function
#
#
# @my_func
# def culc(i):
#     print(i ** i ** i)
#
#
# if __name__ == '__main__':
#     culc(4)
import time
from functools import wraps

ATTEMPTS = 3
TIMEOUT = 0.3


def with_attempt(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        error = None
        for i in range(ATTEMPTS):

            try:
                return old_function(*args, **kwargs)
            except Exception as er:
                error = er
                print(
                    f'При вызове {old_function.__name__} получена ошибка: {er}')
                time.sleep(TIMEOUT)
        raise error

    return new_function
