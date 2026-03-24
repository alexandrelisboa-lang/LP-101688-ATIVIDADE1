import os 
os.system("cls")

soma = 0
contador = 0
maior = None
menor = None

print("--- Calculadora de Médias (Digite um negativo para sair) ---")

while True:
    valor = int(input("Digite um valor inteiro: "))
    
    if valor < 0:
        break
    
    # Processamento para a média
    soma += valor
    contador += 1
    
    # Lógica para encontrar o Maior e o Menor
    if maior is None or valor > maior:
        maior = valor
    if menor is None or valor < menor:
        menor = valor

# Resultados finais
if contador > 0:
    media = soma / contador
    print("-" * 30)
    print(f"Quantidade de números: {contador}")
    print(f"Média aritmética: {media:.2f}")
    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")
else:
    print("Nenhum valor positivo foi processado.")