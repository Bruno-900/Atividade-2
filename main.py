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