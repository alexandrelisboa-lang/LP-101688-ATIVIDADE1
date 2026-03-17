import os
os.system("cls")
import time

numero=int(input("informe um numero:"))
for i in range (1,11,1):
        tabuada=numero * i
        print("  ")     
        print(f"{numero} x {i}={tabuada}")
        time.sleep(2)