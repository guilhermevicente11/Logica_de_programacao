# -*- coding: utf-8 -*-
"""Variáveis, Entradas e saídas.

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TMcMTXD99v-FfSKYiXNdsjHVbDO4dDb-
"""

#Faça um programa que peça um número e mostre a mensagem "O número informado foi [número]".
numero = int(input("Informe o numero: "))

print(f"O numero informado foi: {numero}.")

#Faça um programa que peça um número para o usuário (string), converta-o para float e depois imprima-o na tela. Você consegue fazer a mesma coisa, porém convertendo para int?
numero = input("Insira seu numero: ")

z = float(numero)

print(f"O numero escolhido foi: {z}.")

numero = input("Insira seu numero: ")

z = int(numero)

print(f"O numero escolhido foi: {z}.")

#Faça um programa que peça dois números inteiros e imprima a soma deles.

numero_1 = int(input("Insira um numero: "))
numero_2 = int(input("Insira outro numero: "))

soma = numero_1 + numero_2

print(f'A soma dos números é: {soma}. ')

#Faça um programa que peça as 4 notas bimestrais de um aluno e mostre a média aritmética delas.

nota_1 = float(input("Nota do primeiro bimestre: "))
nota_2 = float(input("Nota do segundo bimestre: "))
nota_3 = float(input("Nota do terceiro bimestre: "))
nota_4 = float(input("Nota do quarto bimestre: "))

nota_total = (nota_1 + nota_2 + nota_3 + nota_4)

media = (nota_total) / 4

print(f"A media do aluno no ano foi: {media}.")

#Faça um programa que peça o raio de um círculo, calcule e mostre sua área.

raio_circulo = float(input("Informe o raio do circulo: "))

area_circulo = 3.14*(raio_circulo)**2

print(f"A area do circulo é: {area_circulo}.")

# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês e depois, calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input("Qual seu salario por hora trabalhada?: "))
hora_trabalhada = float(input("Quantas horas você trabalha no mês?: "))

total_salario = valor_hora * hora_trabalhada

print(f"Seu salário no mês é de: {total_salario}.")

# Transforme Fahrenheit em CELSIUS.

temperatura_far = float(input("Informe a temperatura em graus Fahrenheit: "))

conversao_cel = (temperatura_far - 32) / 1.8

print(f"A temperatura de {temperatura_far} Fahrenheit é igual a {conversao_cel} em Celsius")

#Transformar CELSIUS em FAHRENHEIT

temperatura_cel = float(input("Informe a temperatura em graus celsius: "))

conversao_far = (1.8*temperatura_cel) + 32

print(f"A temperatura de {temperatura_cel} Celsius é igual a {conversao_far} em Fahrenheit")

# Faça um programa que peça o dia, o mês e o ano para o usuário e imprima a data completa no formato dd/mm/aaaa.
#INCOMPLETO

dia = int(input("Informe o dia de nascimento: "))
mes = int(input("Informe o mes de nascimento: "))
ano = int(input("Informe o ano de nascimento: "))


print(f"A data de nascimento é:{dia}/{mes}/{ano}.")

#Faça um programa que peça 2 números inteiros e um número real, calcule e mostre:
# o produto do dobro do primeiro com metade do segundo.
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

primeiro_numero = int(input("Digite um numero inteiro: "))
segundo_numero = int(input("Digite um numero inteiro: "))
terceiro_numero = float(input("Digite um numero real: "))

resposta_1 = (primeiro_numero * 2) * (segundo_numero / 2)
resposta_2 = (primeiro_numero * 3) + (terceiro_numero)
resposta_3 = (terceiro_numero) ** 3

print(f"O produto do dobro do primeiro com metade do segundo é: {resposta_1}.")
print(f"A soma do triplo do primeiro com o terceiro é: {resposta_2}.")
print(f"O terceiro elevado ao cubo é: {resposta_3}.")

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = (peso)/(altura)**2

resultado_imc = round(imc, 2)

print(f"Seu imc é: {resultado_imc}")

valor = float(input("Digite o valor monetário: "))

acrescimo = (valor*1.15)

acrescimo_arredondado = round(acrescimo)

print(f"O novo valor é de: {acrescimo_arredondado}")

valor = float(input("Digite o valor monetário: "))

decrescimo = (valor) - (valor * 0.15)

decrescimo_arredondado = round(decrescimo)

print(f"O novo valor é de: {decrescimo_arredondado}")

# Sorvetao MUV - Vertical
# Digitar uma velocidade inicial (em m/s), uma posição inicial (em m) e um instante de tempo (em s) e imprima a posição de um projétil nesse instante de tempo.

y0 = float(input("Digite a posição inicial do projetil em metros: "))
v0 = float(input("Digite a velocidade inicial di projétil em m/s: "))
t = float(input("Digite o instante de tempo desejado em segundos: "))

posicao_projetil = y0 + (v0*t) + (-10*(t**2) / 2)

print(f"A posição do projetil é: {posicao_projetil}.")

from datetime import datetime

data_hora = datetime.now()

print(data_hora)

