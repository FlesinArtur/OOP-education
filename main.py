import time


def stopwatch(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start
        print(*args, **kwargs)
        print(f"Time of function end: {end}")
        return result
    return wrapper


def list_count(count):
    def list_count_(func):
        def wrapper(*args, **kwargs):
            result = []
            for i in range(count):
                result.append(func(*args, **kwargs))
            return print(result)
        return wrapper
    return list_count_


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

    @stopwatch
    def __add__(self, value):
        return Number(self.number + value.number)

    @stopwatch
    def __sub__(self, value):
        return Number(self.number - value.number)

    @list_count(3)
    def __mul__(self, value):
        return Number(self.number * value.number)

    def __truediv__(self, value):
        return Number(self.number / value.number)

    def __eq__(self, value):
        return self.number == value


def main():
    mynumber = Number('12')
    mynumber1 = Number(6)
   #print(mynumber)
   #print(mynumber1)
    my_value = mynumber + mynumber1
    my_value = mynumber * mynumber1
   #my_value = mynumber - mynumber1
   #my_value = mynumber / mynumber1
   #print(f'{mynumber1.x}=')    # f-strings
   #print(f'{mynumber1.x=}')    # print(f'mynumber1.x={mynumber1.x}')


def test():
    print('Test!')


if __name__ == "__main__":

    main()
