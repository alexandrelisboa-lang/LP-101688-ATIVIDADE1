import os
os.system("cls")

#MENU
print("""
==============MENU============
codigo     prato        valor

  1       picanha        25,00
  2       lasanha        20,00
  3       strogonoff     18,00
  4       bife acebolado 15,00
  5       pao com ovo     5,00
      
      
      
      
      
      
      
""")
prato =int(input("escolha o prato desejado digitando o codigo: "))

match prato:
    case 1:
     print("voce escolheu picanha e o valor do pra e 25,00" )
    case 2:
     print("voce escolheu lasanha e o valor do pra e 20,00" )
    case 3:
     print("voce escolheu strogonoff e o valor do pra e 18,00" )
    case 4:
     print("voce escolheu bife acebolado e o valor do pra e 15,00" )
    case 5:
     print("voce escolheu pao com ovo e o valor do pra e 5,00" )
    case _:
        print("opiçao invalida" )
    
    
    