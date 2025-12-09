import sys
import time
import cmath
from calculator import ComplexCalculator

CONSTANTS = {
    "pi": cmath.pi,
    "euler": cmath.e,
}

def get_number_input(prompt):
    """
    Helper to get a float number from user input.
    Supports 'pi' and 'euler'.
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in CONSTANTS:
            return CONSTANTS[user_input]
        try:
            return float(user_input)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número, 'pi' ou 'euler'.")

def get_complex_number(ordinal):
    """
    Prompts user for real and imaginary parts to construct a complex number.
    """
    print(f"\n--- Definindo o {ordinal} número complexo ---")
    real = get_number_input("Digite o número real: ")
    imag = get_number_input("Digite o número imaginário: ")
    return complex(real, imag)

def show_menu():
    print("\n------------------------------")
    print("[1] Conjugado")
    print("[2] Adição")
    print("[3] Subtração")
    print("[4] Multiplicação")
    print("[5] Divisão")
    print("------------------------------")
    return input("Digite qual operação deseja utilizar: ").strip()

def show_post_op_menu():
    print("\n------------------------------")
    print("[1] Sair da Calculadora")
    print("[2] Reiniciar (Novos números)")
    print("[3] Usar resultado anterior como primeiro número")
    print("------------------------------")
    return input("Escolha uma opção: ").strip()

def main():
    print("Bem-vindo à Calculadora de Números Complexos!")
    
    # Initial state
    z1 = None
    
    while True:
        # If z1 is not set (start or restart), ask for it
        if z1 is None:
            z1 = get_complex_number("primeiro")
        
        choice = show_menu()
        
        result = None
        
        if choice == "1":
            result = ComplexCalculator.conjugate(z1)
            print(f"\nO conjugado é: {result}")
        elif choice in ["2", "3", "4", "5"]:
            z2 = get_complex_number("segundo")
            try:
                if choice == "2":
                    result = ComplexCalculator.add(z1, z2)
                    op_name = "soma"
                elif choice == "3":
                    result = ComplexCalculator.subtract(z1, z2)
                    op_name = "subtração"
                elif choice == "4":
                    result = ComplexCalculator.multiply(z1, z2)
                    op_name = "multiplicação"
                elif choice == "5":
                    result = ComplexCalculator.divide(z1, z2)
                    op_name = "divisão"
                
                print(f"\nA {op_name} dos complexos é: {result}")
            except ValueError as e:
                print(f"\nErro: {e}")
                continue
        else:
            print("\nOpção inválida. Tente novamente.")
            continue
            
        time.sleep(1)
        
        # Post-operation loop
        while True:
            post_choice = show_post_op_menu()
            if post_choice == "1":
                print("Até logo!")
                sys.exit(0)
            elif post_choice == "2":
                print("Reiniciando...")
                z1 = None # Reset z1 to trigger fresh inputs
                break # Break post-op loop, go to main loop
            elif post_choice == "3":
                if result is not None:
                    z1 = result
                    print(f"Usando {z1} como o primeiro número complexo.")
                    break # Break post-op loop, go to main loop with z1 set
                else:
                    print("Nenhum resultado anterior disponível. Reiniciando...")
                    z1 = None
                    break
            else:
                print("Opção inválida.")
        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSaindo...")
        sys.exit(0)
