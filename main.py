import cmath
import sys
import time

import numpy as np

PI = cmath.pi
EULER = cmath.e


class Operations:
    def __init__(self, z1):
        self.z1 = z1

    def conjugated(self):
        conj = np.conj(self.z1)
        return conj

    def addition(self, z2):
        add = self.z1 + z2
        return add

    def subtraction(self, z2):
        sub = self.z1 - z2
        return sub

    def multiplication(self, z2):
        mult = self.z1 * z2
        return mult

    def division(self, z2):
        div = self.z1 / z2
        return div


class Helper:
    def convert_to_float(user_number):
        pi_or_euler = {
            "pi": PI,
            "euler": EULER,
        }

        if user_number in pi_or_euler:
            return pi_or_euler[user_number]
        else:
            return float(user_number)

    def exit_calc():
        return sys.exit("Até logo!")


def complex_z1():
    re1 = input("Digite o número real do primeiro complexo: ")
    im1 = input("Digite o número imaginario do primeiro complexo: ")

    real = Helper.convert_to_float(re1)
    imag = Helper.convert_to_float(im1)

    z1 = complex(real, imag)

    return z1


def complex_z2():
    re2 = input("Digite o número real do segundo complexo: ")
    im2 = input("Digite o número imaginario do segundo complexo: ")

    real_2 = Helper.convert_to_float(re2)
    imag_2 = Helper.convert_to_float(im2)

    z2 = complex(real_2, imag_2)

    return z2


def choices():
    print("")
    print("[1] Conjugado\n[2] Adição\n[3] Subtração\n[4] Multiplicação\n[5] Divisão")
    print("")
    choice = input("Digite qual operação deseja utilizar: ")

    return choice


def second_choices(choice, result=None):
    if choice != "1":
        if result is None:
            z2 = complex_z2()

        else:
            z2 = complex_z2()

            if choice == "2":
                result = operation.addition(z2)
                print("A soma dos complexos é: ", result)
                time.sleep(2)

                new_options(result)

            elif choice == "3":
                result = operation.subtraction(z2)
                print("A subtração dos complexos é: ", result)
                time.sleep(2)

                new_options(result)

            elif choice == "4":
                result = operation.multiplication(z2)
                print("A multiplicação dos complexos é: ", result)
                time.sleep(2)

                new_options(result)

            elif choice == "5":
                result = operation.division(z2)
                print("A divisão dos complexos é: ", result)
                time.sleep(2)

                new_options(result)


def new_options(result):
    print("")
    print(
        "[1] Sair da Calculadora.\n[2] Reiniciar Calculadora.\n[3] Realizar operação com o resultado anterior."
    )
    print("")
    choice_final = input("Digite qual operação deseja utilizar: ")
    if choice_final == "1":
        print("Saindo...")
        time.sleep(2)
        Helper.exit_calc()
    elif choice_final == "2":
        print("Reiniciando a calculadora...")
        time.sleep(2)
        print("")
    elif choice_final == "3":
        choice = choices()
        if choice == "1":
            print("O conjugado é: ", result)
            time.sleep(2)
            new_options(result)

        else:
            operation.z1 = result
            second_choices(choice, result)


my_bool = True

while my_bool:
    z1 = complex_z1()
    operation = Operations(z1)

    choice = choices()

    if choice == "1":
        result = operation.conjugated()
        print("O conjugado é: ", result)
        time.sleep(2)

        new_options(result)

    else:
        second_choices(choice, result=z1)
