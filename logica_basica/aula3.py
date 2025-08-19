"""
Python = Linguagem de Programação
Tipo de tipagem = dinâmica / forte
str -> string -> texto
Strings são textos que estão dentro de aspas
"""
print(12345)

# Aspas Simples
print('Lucas Teixeira')

# Aspas Duplas
print("Lucas Teixeira")

# Escape
print("Lucas \"Teixeira\"")

# raw string
print(r"Lucas \"Teixeira\"")

# Maneira clean code, sem usar escape ou r
print('Lucas "Teixeira"')
print(1, 'Lucas "Teixeira"')
print(2, "Lucas 'Teixeira'")

print(end='\n')

texto = '''Este é um exemplo de string
    que abrange várias linhas.
    A quebra de linha é feita
    automaticamente.'''

print(texto)
