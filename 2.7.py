# Armazenando um nome em uma variável com vários espaços desnecessários
nome = '   john      '

# Printando esse nome e utilizando métodos para retirar os espaços
print(nome.strip() + '\n' + nome.rstrip() + '\n' + nome.lstrip())
