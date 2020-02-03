# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

print("")

print("Selecione a opção desejada:")

print("")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")


opcao=int(input("Digite a opção desejada: 1/2/3/4 "))
print(" ")

if opcao == 1:
    print("OPÇÃO ---- SOMA ---- ")
    print(" ")
    num1=(int(input("Digite o primeiro numero: ")))
    num2=(int(input("Digite o segundo  numero: ")))      
    Soma=num1+num2
    print("Total da soma: ", Soma)
elif opcao ==2:
    print("OPÇÃO ---- Subtração ---- ")
    print(" ")
    num1=(int(input("Digite o primeiro numero: ")))
    num2=(int(input("Digite o segundo  numero: ")))    
    Subtracao = num1 - num2
    print("Total da Subtração: ", Subtracao)
elif opcao == 3:
    print("OPÇÃO ---- Multiplicação ---- ")
    print(" ")
    num1=(int(input("Digite o primeiro numero: ")))
    num2=(int(input("Digite o segundo  numero: ")))         
    Multiplicacao= num1 * num2
    print("Total da Multiplicação: ", Multiplicacao)
elif opcao == 4:
    print("OPÇÃO ---- Divisão ---- ")
    print(" ")
    num1=(int(input("Digite o primeiro numero: ")))
    num2=(int(input("Digite o segundo  numero: ")))             
    Divisao = num1 / num2
    print("Total da Divisão: ", Divisao)
else:
    print("Opção inválida")
          