# Lista em forma de tupla com alguns valores
pratos = ('lasanha', 'macarronada', 'pizza', 'nhoque', 'strogonoff')

# Printando a tupla com os determinados valores da lista
print('Nosso restaurante oferece as seguintes opções:')
for pratos in pratos:
    print(pratos.title())

# Sobrescrevendo a tupla com dois valores alterados
pratos = ('lasanha', 'macarronada', 'calzone', 'panqueca', 'strogonoff')

# Printando os novos valores
print('\nO cardápio sofreu uma leve alteração, e agora estas são as opções disponíveis:')
for pratos in pratos:
    print(pratos.title())