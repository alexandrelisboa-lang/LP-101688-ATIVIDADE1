import os 
os.system("cls")
import time

soma= 0 
QUANTIDADE_NOTAS =3

for i in range(QUANTIDADE_NOTAS):
    nota = float(input("digite uma nota: "))
    soma+= nota

media = soma / QUANTIDADE_NOTAS

if media >= 7:
    resutado = "aprovado"
elif media <= 4:
    resultado = "reprovado"
else:
    resultado = "recuperaçao"

    print(f"media: {media}")
    print(f"resultado:{resultado} ")

