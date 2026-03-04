import os
os.system("cls")
#ENTRADA


login_do_usuario = input("digite seu login: ")
senha_do_usuario =input("digte sua senha: ")

login_correto=("xandy123")
senha_correta=("xandinho123")

if login_do_usuario == login_correto and senha_do_usuario == senha_correta:
      print("bem-vindo")
  
else:
     print("login ou senha invalida")

