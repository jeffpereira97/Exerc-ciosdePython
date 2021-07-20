# Lista contendo os valorez utilizados
minhas_pizzas = ['calabresa', 'strogonoff', 'cinco queijos']

# Copiando os valores da lista minhas_pizzas para outra lista
outras_pizzas = minhas_pizzas[:]

# Adicionando um sabor de pizza a lista minhas_pizzas
minhas_pizzas.append('mignon no barbecue')

# Adicionando um sabor de pizza a lista outras_pizzas
outras_pizzas.append('catuperony')

# Printando a primeira lista de pizzas
print('Minhas pizzas favoritas são: ')
for minhas_pizzas in minhas_pizzas:
    print(minhas_pizzas.title())

# Printando a segunda lista de pizzas
print('\nAs pizzas favoritas de meu amigo são: ')
for outras_pizzas in outras_pizzas:
    print(outras_pizzas.title())
