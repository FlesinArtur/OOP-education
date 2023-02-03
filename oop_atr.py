class A:
    x = 1

    def __init__(self, value):
        self.x = value


if __name__ == '__main__':
    a = A(5)
    print(f'{a.__class__.x=}')
    print(f'{a.x=}')
    print(f'{A.x=}')

    a.x = 10

    print(f'{a.x=}')
    print(f'{A.x=}')

    A.x = 15

    print(f'{a.x=}')
    print(f'{A.x=}')
