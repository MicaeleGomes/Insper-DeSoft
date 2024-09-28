# Escreva um programa que pergunta para o usuário o valor da conta do restaurante e imprime: "Valor da conta com 10%: R$ X.YZ", 
# onde X.YZ é o valor da conta mais os 10% com exatamente duas casas decimais.

valor_conta = float(input("Qual foi o valor da conta?: "))

valor_total = valor_conta + (0.10 * valor_conta)

print ("Valor da conta com 10%: R$ {0:.2f}".format(valor_total))
