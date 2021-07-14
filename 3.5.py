from time import sleep
convidados = ['john', 'sarah', 'sam']
print('Saudações, ' + convidados[0].title() + '. Você está convidado para um jantar amanhã.')
print('Saudações, ' + convidados[1].title() + '. Você está convidado para um jantar amanhã.')
print('Saudações, ' + convidados[2].title() + '. Você está convidado para um jantar amanhã.')

sleep(2)

print('Infelizmente, ' + convidados[0].title() + ' não poderá comparecer para o jantar')
convidados[0] = 'adam'
print('Saudações, ' + convidados[0].title() + '. Você está convidado para um jantar amanhã.')
print('Saudações, ' + convidados[1].title() + '. Você está convidado para um jantar amanhã.')
print('Saudações, ' + convidados[2].title() + '. Você está convidado para um jantar amanhã.')