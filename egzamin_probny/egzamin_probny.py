"""Zadanie 1"""
from math import pi


def calc_circle_area(r):
    print(r * r * pi)


calc_circle_area(5)

"""Zadanie2"""


def check_parity():
    number1 = int(input("Enter a number :"))
    if number1 % 2 == 0:
        print("Your number is even")
    else:
        print("Your number is odd")


check_parity()

"""Zadanie3"""


def element_present(number2, array):
    if number2 in array:
        # result=True
        print(True)
    else:
        # result=False
        print(False)


element_present(15, [1, 2, 3, 4, 5, 6])

"""Zadanie4"""


def check_str_len():
    string1 = input("Enter a string : ")
    try:
        if len(string1) <= 8:
            raise ValueError
        else:
            print("OK")

    except ValueError:
        print("Value error")


check_str_len()

"""Zadanie5"""

slownik = {}


def print_menu():
    print("1.Dodaj wpis :")
    print("2. Odzyskaj wpis :")
    print("3. Zmodyufikuj wpis: ")
    print("4.Usun wpis : ")
    print("0. Wyjdz z programu")


def create_item(dict1, key, value):
    # print(slownik)
    dict1[key] = value
    # print(slownik)


def read_item():
    print(slownik)


def update_item(dict1, key, updated_value):
    # print(dict1)
    dict3 = {key: updated_value}
    dict1.update(dict3)
    # print(dict1)


def delete_item(dict1, key):
    # print(dict1)
    dict1.pop(key)
    # print(dict1)


while True:
    print_menu()
    option = input('Podaj opcja :')
    if option == "1":
        create_item(slownik, input("Podaj key:"), input('Podaj value '))

    elif option == '2':
        read_item()

    elif option == '3':
        update_item(slownik, input('Podaj key'), input('Podaj nowe value'))

    elif option == "4":
        delete_item(slownik, input("Podaj key "))

    elif option == "0":
        break

"""Zadanie6"""


class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)

    def set_name(self, name):
        self.name = name


class Mammal(Animal):
    def __init__(self, no_legs, has_fur, name):
        super.__init__(self, name)
        self.no_legs = no_legs
        self.has_fur = has_fur

    def get_no_legs(self):
