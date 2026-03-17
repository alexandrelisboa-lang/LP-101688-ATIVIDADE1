import os
os.system("cls")


while  True:
     idade = int(input("digite sua idade: "))
     if idade < 18:
          print("acesso negado!")
          print("tente novamente--- \n")
     else:
          print("acesso permitido.")
          break
     print(" fim ")
