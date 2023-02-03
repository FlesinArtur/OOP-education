import sys


class A:
    x = 2
    pass


class B:
    x = 1
    pass


class Number(A, B):
    def __init__(self, number):
        self.number = number
        if type(number) is not int:
            try:
                self.number = int(number)
            except (ValueError, TypeError):
                raise Exception("Неправильно введені дані!")
        print(f"Number ({number})")

    def __str__(self):
        return f"Number({self.number})"

    def __add__(self, value):
        return Number(self.number + value.number)

    def __sub__(self, value):
        return Number(self.number - value.number)

    def __mul__(self, value):
        return Number(self.number * value.number)

    def __truediv__(self, value):
        return Number(self.number / value.number)

    def __eq__(self, value):
        return self.number == value


def main():
    mynumber = Number('12')
    mynumber1 = Number(6)
    print(mynumber)
    print(mynumber1)
    my_value = mynumber + mynumber1
    my_value = mynumber * mynumber1
    my_value = mynumber - mynumber1
    my_value = mynumber / mynumber1

    print(f'{mynumber1.x}=')    # f-strings
    print(f'{mynumber1.x=}')    # print(f'mynumber1.x={mynumber1.x}')


def test():
    print('Test!')


if __name__ == "__main__":
    a = test

    # print(test == a)

    # The same
    print(id(test) == id(a))
    print(test is a)

    # main()
