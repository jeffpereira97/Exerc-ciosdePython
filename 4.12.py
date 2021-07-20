# Lista contendo os valorez utilizados
my_foods = ['pizza', 'falafel', 'carrot cake']

# Copiando os valores da lista my_foods para outra lista
friend_foods = my_foods[:]

# Adicionando um sabor de pizza a lista my_foods
my_foods.append('cannoli')

# Adicionando um sabor de pizza a lista friend_foods
friend_foods.append('ice cream')

# Printando a primeira lista de valores
print('My favorite foods are: ')
for my_foods in my_foods:
    print(my_foods.title())

# Printando a segunda lista de valores
print("\nMy friend's favorite foods are: ")
for friend_foods in friend_foods:
    print(friend_foods.title())
