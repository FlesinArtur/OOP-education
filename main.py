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

    def __add__(self, value):
        print(self.number + value.number)


def main():
    mynumber = Number(6)
    mynumber1 = Number(6)
    mynumber + mynumber1


if __name__ == "__main__":
    main()
