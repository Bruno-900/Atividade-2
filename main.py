# Universidade Mogi das Cruzes
# Atividade 2 (CRUD) Sofware Basico

import datetime                 #biblioteca para formater data e hora.
import os                       #biblioteca para a limpar o console.
from tabulate import tabulate   #biblioteca para formataçao no console. 

lista = []                      #criando uma lista vazia.
dicionario = {}                 #criando um dicionario vazio.

#função para salvar os no repositorio txt.

def salvar_no_txt(dicionario):                                          
    with open("repositorio.txt", "w") as repositorio:
        for principal, secundario in dicionario.items():
            repositorio.write(f'{principal},{secundario[0]},{secundario[1]},{secundario[2]},{secundario[3]},{secundario[4]},{secundario[5]}\n')

#função para carregar o repositorio txt.

def carregar_do_txt():
    try:
        with open("repositorio.txt", "r") as repositorio:
            for linha in repositorio:
                itens = linha.strip().split(",")
                lista.append(itens)
                dicionario[itens[0]] = itens[1:7]

    #caso o arquivo ainda não tenha sido criado.
    
    except FileNotFoundError:
        print("Arquivo de repositório não encontrado. Um novo será criado.")

carregar_do_txt()

#função para mostar apenas um registro especifico.

def mostrar_registro_tabela(registro, dicionario):
    if registro in dicionario: 
        tabela = [["Registro", "Nome", "CPF", "Destino", "Data", "Horário", "Peso(Kg)"]] 
        tabela.append([registro, *dicionario[registro]])

        #Usando a biblioteca tabulate para formater

        print(tabulate(tabela, headers="firstrow", tablefmt="grid", colalign=("left", "left", "left", "left", "left", "left", "left"))) 
    
    else: print("Registro não encontrado!")

#função para excluir um registro.

def excluir_registro(registro, lista):
    for index, item in enumerate(lista):
        if item[0] == registro:
            return index
    return None

#função para buscar um registro pelo cpf.

def buscar_cpf(cpf, lista):
    for item in lista:
        if str(item[2]) == cpf:
            return item
    return None

#loop principal.

while True:

    entrada = input('''
        SISTEMA DE CONTROLE DE BAGAGENS
-----------------------------------------------
(1) Incluir registro de bagagem
(2) Excluir registro de bagagem
(3) Alterar registro de bagagem
(4) Pesquisa por CPF
(5) Relatório geral
(6) SAIR
------------------------------------------------
==>''')

    #correçao erro de digitação errada do usuario.

    if entrada not in ('1', '2', '3', '4', '5', '6'):
        
        os.system("cls" if os.name == "nt" else "clear")
        
        print("Opção inválida. Tente novamente")
        continue

    if entrada == '1':
        
        os.system('cls')
        
        while True:

            
            registro = input("Digite o número do registro da bagagem (até 5 dígitos): ")
    

            if registro in dicionario:
                
                os.system('cls')
                print("Esse registro ja existe !")
                continue 
    
            #Colocando uma opçao de registro apenas com numeros e um total de 99999 possibilidades de registros.
            #(pode ser alterado para mais ou menos).

            elif registro.isdigit() and len(registro) < 5:

                 registro_convertido = registro 
                 break
            
            else:
                
                os.system('cls')
                print("Entrada inválida! Por favor, digite exatamente cinco dígitos.")
                continue
        
        os.system('cls')
        
        nome = input("Digite o nome do passageiro: ")
        
        os.system('cls')
        
        while True:
            
            cpf = input("Digite o CPF do passageiro (onze dígitos): ")
            
            #colocando um numero exato que deve serdigitado para o CPF(onze digitos).

            if cpf.isdigit() and len(cpf) == 11:
                cpf_convertido = int(cpf)
                break   
            
            else:
                os.system('cls')
                print("Inválido! Digite novamente")
        
        os.system('cls')
        
        destino = input("Digite o destino do Passageiro: ")

        os.system('cls')
        
        while True:
            
            data = input("Digite a data da viagem (DD/MM/AAAA): ")
            
            try:

                #usando biblioteca 'datetime' prara padronizar a data.

                data_convertida = datetime.datetime.strptime(data, "%d/%m/%Y").date() 
                data_lista = data_convertida.strftime("%d/%m/%Y")
                break
            
            except ValueError:
                os.system('cls')
                print("Inválido! Digite novamente.")
        
        os.system('cls')
        
        while True:
            
            horario = input("Digite o horário no formato (HH:MM): ")
            
            try:

                #usando biblioteca datetime prara padronizar a hora.

                horario_convertido = datetime.datetime.strptime(horario, "%H:%M").time() 
                horario_lista = horario_convertido.strftime("%H:%M")
                break
            
            except ValueError:
                os.system('cls')
                print("Inválido! Digite novamente.")
        
        os.system('cls')
        
        while True:
            
            try:

                #usando float para um numemero mais exato do peso.

                peso = float(input("Digite o peso da bagagem(KG): "))
                break
            
            except ValueError:
                os.system('cls')
                print("Inválido! Digite novamente.")
        
        #Salvando todos os itens em uma lista 

        lista.append([registro_convertido, nome, cpf_convertido, destino, data_lista, horario_lista, peso])
        
        #Criando o dicionario

        dicionario[registro_convertido] = [nome, cpf_convertido, destino, data_lista, horario_lista, peso]
        
        #Usando a função de salvar no txt.

        salvar_no_txt(dicionario)

        #Mostrando os registro no terminal.
        
        mostrar_registro_tabela(registro, dicionario)
        
        print("Registro adicionado!")
        
        input("Aperte ENTER para voltar")
        
        os.system('cls')

    if entrada == '2':
        
        os.system('cls')
        
        while True :
            
            registro = input("Digite o número do registro da bagagem (cinco dígitos): ")
            mostrar_registro_tabela(registro, dicionario)         
            
            indice = excluir_registro(registro, lista)
            
            if indice is None:
                print("Esse registro não existe")
                break
            
            else:
                
                confirmacao = input("Deseja realmente excluir este registro? (S/N): ").strip().lower() 
                
                if confirmacao == 's':
                    del lista[indice]
                    del dicionario[registro]
                    salvar_no_txt(dicionario)
                    print("Registro da bagagem excluído")
                    break

                else :
                    os.system('cls')
                    print("Exclusão cancelada!")
                    break

    if entrada == '3':
        
        os.system('cls')
        
        registro = input("Digite o número do registro da bagagem que será alterada (cinco dígitos): ")
        
        if registro not in dicionario:
            print("Esse registro não foi encontrado! Tente novamente!")
            continue

        if registro in dicionario:
            
            mostrar_registro_tabela(registro, dicionario)

        while True:
            
            campo = input('''
Qual campo deseja alterar?
1. Nome
2. CPF
3. Destino
4. Data
5. Horário
6. Peso
7. Sair
''')

            #correçao erro de digitação errada do usuario.

            if campo not in ('1', '2', '3', '4', '5', '6', '7'):
                print("Opção inválida. Tente novamente.")
                continue

            if campo == '1':
                
                os.system('cls')
                mostrar_registro_tabela(registro, dicionario)
                novo_nome = input("Digite o novo nome: ")
                dicionario[registro][0] = novo_nome
            
            elif campo == '2':
                
                while True:
                    
                    os.system('cls')
                    mostrar_registro_tabela(registro, dicionario)
                    novo_cpf = input("Digite o novo CPF (onze dígitos): ")
                    
                    if novo_cpf.isdigit() and len(novo_cpf) == 11:
                        dicionario[registro][1] = int(novo_cpf)
                        break
                    
                    else:
                        os.system('cls')
                        print("Inválido! Digite novamente.")
            
            elif campo == '3':
                
                os.system('cls')
                mostrar_registro_tabela(registro, dicionario)
                novo_destino = input("Digite o novo destino: ")
                dicionario[registro][2] = novo_destino
            
            elif campo == '4':
                
                while True:
                    
                    os.system('cls')
                    mostrar_registro_tabela(registro, dicionario)
                    nova_data = input("Digite a nova data (DD/MM/AAAA): ")
                    
                    try:
                        data_convertida = datetime.datetime.strptime(nova_data, "%d/%m/%Y").date()
                        dicionario[registro][3] = data_convertida.strftime("%d/%m/%Y")
                        break
                    
                    except ValueError:
                        os.system('cls')
                        print("Inválido! Digite novamente.")
            
            elif campo == '5':
                
                while True:
                    
                    os.system('cls')
                    mostrar_registro_tabela(registro, dicionario)
                    novo_horario = input("Digite o novo horário (HH:MM): ")
                    
                    try:
                        horario_convertido = datetime.datetime.strptime(novo_horario, "%H:%M").time()
                        dicionario[registro][4] = horario_convertido.strftime("%H:%M")
                        break
                    
                    except ValueError:
                        os.system('cls')
                        print("Inválido! Digite novamente.")
            
            elif campo == '6':
                
                os.system('cls')
                mostrar_registro_tabela(registro, dicionario)
                novo_peso = float(input("Digite o novo peso: "))
                dicionario[registro][5] = novo_peso
            
            elif campo == '7':
                os.system('cls')
                break
            
            salvar_no_txt(dicionario)
            os.system('cls')
            mostrar_registro_tabela(registro, dicionario)
            print("Campo alterado com sucesso!")

    if entrada == '4':
        
        os.system('cls')
        
        cpf = input("Digite o CPF do passageiro: ")
        resultado = buscar_cpf(cpf, lista)
        
        if resultado is None:
            print("CPF não encontrado")
        
        else:

            #usando a biblioteca tabulate para formatar.

            print(tabulate([resultado], headers=["Registro", "Nome", "CPF", "Destino", "Data", "Horário", "Peso"], tablefmt="grid", colalign=("left", "left", "left", "left", "left", "left", "left")))
            input("aperte ENTER para sair")
            os.system('cls')

    if entrada == '5':
        
        os.system('cls')
        
        tabela = [["Registro", "Nome", "CPF", "Destino", "Data", "Horário", "Peso(Kg)"]]
        for principal, secundarios in dicionario.items():
            tabela.append([principal, *secundarios])

        #usando a biblioteca tabulate para formatar.
    
        print(tabulate(tabela, headers="firstrow", tablefmt="grid", colalign=("left", "left", "left", "left", "left", "left", "left")))
        input("Aperte ENTER para sair")
        os.system('cls')

#sair do programa

    if entrada == '6':
        
        os.system('cls')
        break

# fim do programa

print("FIM DO PROGRAMA")

#Universidade mogi das Cruzes 30/09/2024
#Atividade Software Basico

#Blibioteca com a função os.system('cls') de limpeza do console.

import os

#Função usando "listas" com os preços e quartos disponiveis

def diaria(quarto, pessoas, dias) :

    Q1 = [20.00, 28.00, 35.00, 42.00, 48.00, 58.00]
    Q2 = [25.00, 34.00, 42.00, 50.00, 57.00, 63.00]

    if pessoas <= 0 :
        return("Valor invalido")
    elif pessoas >= 7 :
        return("Numero de pessoas acima do limite !")
    elif quarto == 1 :
        diaria = Q1[pessoas - 1]
    elif quarto == 2 :
        diaria = Q2[pessoas - 1]
    elif quarto == 0:
        return("Valor invalido !")
    elif quarto >= 3 :
        return("Quarto indisponivel !")
    elif dias < 1 :
        return("opção invalida")
    
    tempo = diaria * dias
    return tempo

#Funçao com a tabela de precos e quartos disponiveis para o usuario.

def tabela_precos():
    return('''Bem vindo à hospedagem :
------------------------------------------------------------------------------------------
tabela de preço - Quarto 1 ()
------------------------------------------------------------------------------------------
R$ 20,00
R$ 28,00 
R$ 35,00
R$ 42,00
R$ 48,00
R$ 53,00
------------------------------------------------------------------------------------------
tabela de preço - Quarto 2 ()
------------------------------------------------------------------------------------------
R$ 25,00
R$ 34,00
R$ 42,00
R$ 50,00
R$ 57,00
R$ 63,00
------------------------------------------------------------------------------------------
          ''')

#Armazenando a tabela de preços dentro de uma variavel

tabela = tabela_precos()

#Repetição caso o usuario queira fazer uma outra reserva.

while True :
    
    os.system
    print(tabela)

    #entrada de dados.

    try:
        pessoas = int(input("Digite a quantidade de pessoas que se hospedarão em sua estadia :"))
        quarto = int(input("Digite o quarto em que ira hospedar-se '1 ou 2' : "))
        dias = int(input("Dgite quantos dias deseja hospedar-se :"))
    
    #Caso o usuario digite qualquer coisa que nao seja numeros.

    except ValueError:
        print("Por favor digite apenas '1' ou '2'.")

        repetir1 = input("Deseja fazer outra estadia ? Digite 1 \nOu digite '2' para finalizar : ")

        os.system("cls")
        if repetir1.lower() == '1' :
            continue
        
        elif  repetir1.lower() == '2' :
            break

        else:
            print("Por favor digite apenas '1' ou '2'.")
            continue

    #Chamando a função e armazenando em uma variavel

    estadia = diaria(quarto, pessoas, dias)

    #Mostar no console caso o usuario digite um numero de quarto indisponivel ou um numero de pessoas acima do limite. E limpa o console para uma nova estadia.
     
    if isinstance(estadia, str):
        os.system('cls')
        print(tabela)
        print(estadia)
    
    #Valor final da estadia e confirmaçao da estadia pelo usuario usuario.
    
    else :
        os.system('cls')
        print(f"O valor da sua estadia será: R${estadia:.2f}")
        
        corrigir = input("Pressione '1' para corrigir ou  '2' para confirmar sua estadia:")
    
        if corrigir.lower() == '1' :
            continue

        elif corrigir.lower() == '2' :
    
            print("estadia Comfirmada")

            #Perguntar ao usuário se deseja repetir o processo limpando o console ou finalizar o programa.
    
            repetir2 = input("Deseja fazer outra estadia ? Digite '1' \n Ou digite '2' para finalizar : ")
    
            os.system("cls")
            if repetir2.lower() == '1' :
                continue
                os.system("cls")

            elif repetir2.lower() == '2' :
                break
            
            #Caso o usuario digirte qualquer coisa que não seja '1' ou '2'.

            else :
                print("Por favor digite apenas '1' ou '2', \n Tente novamente!")
                continue
        
        #Caso o usuario digirte qualquer coisa que não seja '1' ou '2'.

        else :
            print("Por favor digite apenas '1' ou '2', \n Tente novamente!")
            continue

#Fim do programa

print("Fim do programa")        
