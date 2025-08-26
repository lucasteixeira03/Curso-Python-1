a = 'A'
b = 'B'
c = 1.1

string = 'a={0} b={1} c={2:.2f}'
formato = string.format(a, b, c)

# Parametro Criado
d = 'D'
e = 'E'
f = 2.2
string = 'b={1} a={0} c={nome3:.2f}'
formato2 = string.format(
    a, b, nome3=f
)

print(formato)
print(formato2)