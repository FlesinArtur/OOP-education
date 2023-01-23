import sys


class Number:

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


def main():
    mynumber = Number('12')
    mynumber1 = Number(6)
    print(mynumber)
    print(mynumber1)
    my_value = mynumber + mynumber1
    my_value = mynumber * mynumber1
    my_value = mynumber - mynumber1
    my_value = mynumber / mynumber1


if __name__ == "__main__":
    main()
