# variaveis são usadas para salvar algo na memória do computador.
# PEP8: inciie variáveis com letras minúsculas, pode usar 
# números e underline _.
# o sinal de = é o operador de atribuição. Ele é usado para atribuir um valor a um nome (variavel).
# Uso: nome_variavel = expressão

nome_completo = 'Lucas Teixeira'
soma = 2 + 2
int_um = bool('1')

print(nome_completo)
print(soma)
print(end='\n')

print(int_um, type(int_um))
print(end='\n')


# TESTE PESSOAL VETOR
vetor = [1, 2, 3, 4, 5]

print('Vetor entre 2 e 5:')
for i in range(2, 5):
    print(vetor[i])

print(end='\n')

nome = 'Lucas'
idade = 21
maior_de_idade = idade >= 18
print('Nome: ', nome, 'Idade: ', idade)
print('É maior?', maior_de_idade)