import os

                                                 
soma_salarios = 0.0
total_pessoas = 0
maior_idade = 0
menor_idade = 9999
mulheres_salario_alto = 0

while True:
   
    print("\n" + "="*30)
    print("      SISTEMA DE PESQUISA")
    print("="*30)
    print("1 | Adicionar pessoa")
    print("2 | Exibir resultados")
    print("3 | Sair")
    print("-"*30)
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("--- Cadastro de Pessoa ---")
        idade = int(input("Idade: "))
        sexo = input("Sexo (M/F): ").strip().upper()
        salario = float(input("Salário: R$ "))

        
        soma_salarios += salario
        total_pessoas += 1

       
        if idade > maior_idade:
            maior_idade = idade
        if idade < menor_idade:
            menor_idade = idade

       
        if sexo == 'F' and salario >= 5000:
            mulheres_salario_alto += 1

        print("\n[Dados salvos com sucesso! Voltando ao menu...]")
        
    elif opcao == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- RESULTADOS DA PESQUISA ---")
        
        if total_pessoas > 0:
            media_salarial = soma_salarios / total_pessoas
            
            print(f"a) Média de salário do grupo: R$ {media_salarial:.2f}")
            print(f"b) Maior idade: {maior_idade} anos | Menor idade: {menor_idade} anos")
            print(f"c) Mulheres com salário >= R$ 5.000,00: {mulheres_salario_alto}")
        else:
            print("Nenhum dado foi inserido ainda.")
        
        input("\nPressione Enter para voltar ao menu...")
        os.system('cls' if os.name == 'nt' else 'clear')

    elif opcao == '3':
        print("Saindo do sistema... Até logo!")
        break
    
    else:
        print("Opção inválida! Tente novamente.")