nome = 'Gabriel Duarte'
altura = 1.80
peso = 90
imc = peso / (altura ** 2)

# EXPLICAÇÃO SOBRE O USO DE F-STRINGS
# As f-strings (formatted string literals) são uma forma de formatar strings de maneira mais legível e concisa.
# Elas permitem incluir expressões dentro de chaves {} e são precedidas pela letra 'f'.
# Isso facilita a inclusão de variáveis e a formatação de valores, como limitar casas decimais.

# outra maneira de usar:
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'Pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
