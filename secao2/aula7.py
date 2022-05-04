# Formatação de Strings

name = 'Josan Johnata'
age = 30
height = 1.76
weight = 98
is_driver = age > 18
imc = round(weight / (height ** 2), 2)
imc_2 = weight / (height ** 2)

print(name, 'tem', age, 'anos de idade e seu IMC é', imc)
# fString é equivalente ao template string do javascript
print(f'{name} tem {age} anos de idade e seu IMC é {imc_2:.2f}')
