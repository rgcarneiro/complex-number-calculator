import cmath
import sys
import time
from typing import Optional

import numpy as np

PI = cmath.pi
EULER = cmath.e


class Operations:
    def __init__(self, z1: complex):
        self.z1 = z1

    def conjugated(self) -> complex:
        return np.conj(self.z1)

    def addition(self, z2: complex) -> complex:
        return self.z1 + z2

    def subtraction(self, z2: complex) -> complex:
        return self.z1 - z2

    def multiplication(self, z2: complex) -> complex:
        return self.z1 * z2

    def division(self, z2: complex) -> complex:
        return self.z1 / z2


class Helper:
    @staticmethod
    def convert_to_float(user_number: str) -> float:
        pi_or_euler = {
            "pi": PI,
            "euler": EULER,
        }

        if user_number in pi_or_euler:
            return pi_or_euler[user_number]
        return float(user_number)

    @staticmethod
    def exit_calc() -> None:
        sys.exit("Até logo!")


def prompt_number(prompt: str) -> float:
    while True:
        user_number = input(prompt).strip().lower()
        try:
            return Helper.convert_to_float(user_number)
        except ValueError:
            print("Entrada inválida. Digite um número válido, 'pi' ou 'euler'.")


def prompt_complex(position: str) -> complex:
    real = prompt_number(f"Digite o número real do {position} complexo: ")
    imag = prompt_number(f"Digite o número imaginario do {position} complexo: ")
    return complex(real, imag)


def prompt_operation_choice() -> str:
    print("")
    print("[1] Conjugado\n[2] Adição\n[3] Subtração\n[4] Multiplicação\n[5] Divisão")
    print("")
    while True:
        choice = input("Digite qual operação deseja utilizar: ").strip()
        if choice in {"1", "2", "3", "4", "5"}:
            return choice
        print("Opção inválida. Escolha uma das opções listadas.")


def prompt_post_action() -> str:
    print("")
    print("[1] Sair da Calculadora.\n[2] Reiniciar Calculadora.\n[3] Realizar operação com o resultado anterior.")
    print("")
    while True:
        choice_final = input("Digite qual operação deseja utilizar: ").strip()
        if choice_final in {"1", "2", "3"}:
            return choice_final
        print("Opção inválida. Escolha uma das opções listadas.")


def execute_operation(choice: str, operation: Operations) -> Optional[complex]:
    if choice == "1":
        return operation.conjugated()

    z2 = prompt_complex("segundo")

    if choice == "5" and z2 == 0:
        print("Não é possível dividir por zero.")
        return None

    if choice == "2":
        return operation.addition(z2)
    if choice == "3":
        return operation.subtraction(z2)
    if choice == "4":
        return operation.multiplication(z2)
    if choice == "5":
        return operation.division(z2)

    return None


def print_result(choice: str, result: complex) -> None:
    operation_names = {
        "1": "conjugado",
        "2": "soma",
        "3": "subtração",
        "4": "multiplicação",
        "5": "divisão",
    }
    print(f"O resultado da {operation_names[choice]} é: {result}")
    time.sleep(2)


def main() -> None:
    while True:
        operation = Operations(prompt_complex("primeiro"))

        while True:
            choice = prompt_operation_choice()
            result = execute_operation(choice, operation)

            if result is None:
                continue

            print_result(choice, result)

            next_action = prompt_post_action()
            if next_action == "1":
                print("Saindo...")
                time.sleep(1)
                Helper.exit_calc()
            elif next_action == "2":
                print("Reiniciando a calculadora...")
                time.sleep(1)
                break
            elif next_action == "3":
                operation = Operations(result)


if __name__ == "__main__":
    main()
