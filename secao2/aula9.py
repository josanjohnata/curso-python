# Condições IF, ELIF e ELSE + Booleanos

if False:
    print('Verdadeiro.')
elif True:
    print('Agora é verdadeiro.')
elif True:
    print('Mais uma verdadeiro.')
else:
    print('Não é verdadeiro.')

# Condições IF, ELIF e ELSE + Operadores relacionais
# == > >= < <= !=
user = input('Digite seu nome: ')
age = input('Digite sua idade: ')
age = int(age)

limit_age = 18

if age >= limit_age:
    print(f'{user} é maior de idade, pode pegar o empréstimo.')
else:
    print(f'{user} NÃO pode pegar o empréstimo.')
