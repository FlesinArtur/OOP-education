import time


def decorator_1(func):
    print('decorator_1 initialize')

    def wrapper(*args, **kwargs):
        start = time.monotonic()
        result = func(*args, **kwargs)
        end = time.monotonic()
        print(f'::::Time execution: {end - start}')
        return result

    print('before end decorator_1')
    return wrapper


@decorator_1
def func(a, b):
    time.sleep(1)
    print(f'{a=} | {b=}')


class Function:
    def __init__(self):
        print('Init start')

    def __call__(self):
        print('Function.__cal__ start and end')


def func_2():
    print('func_2 start and end')


if __name__ == '__main__':
    breakpoint()
    a = Function()
    a()
    # 18, 19 == 30
    # func_2 = decorator_1(func_2)
    # func_2()
    #
    # a = 1
    # func_2.a = 1
    #
    # print(f'{func_2.a=}')

    # start = time.monotonic()
    # func()
    # end = time.monotonic()
    # print(f'Time execution: {end - start}')


