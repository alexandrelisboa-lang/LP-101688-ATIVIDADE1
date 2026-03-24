import os
os.system("cls")


soma = 0
contador = 0
resposta = "S"


while resposta.upper() != "N":
    nota = float(input("Insira a nota: "))
    
    soma += nota
    contador += 1  
    
    resposta = input("Deseja inserir mais uma nota? (S/N): ")

if contador > 0:
    media = soma / contador
    print(f"\nA média aritmética das {contador} notas informadas é: {media:.2f}")
else:
    print("\nNenhuma nota foi inserida.")
    

