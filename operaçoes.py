import os
os.system("cls")

n1 = int(input("digite um numero: "))
n2 = int(input("digite outro numero: "))
oper = input("escolha operaçao desejada: ")

soma = n1+n2
subtraçao = n1 - n2
multiplicaçao = n1 * n2
divisao = n1 / n2

match oper:
    case"+":
        print(f"o resultado foi {soma}")
    case"-":
        print(f"o resultado foi{subtraçao}")
    case"*":
        print(f"o resulatdo foi{multiplicaçao}")
    case"/":
        print(f"o resultado foi{divisao}")
        
print("FIMM")