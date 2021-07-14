# Importação da lib Sleep
from time import sleep

# Primeira lista de comentários
convidados = ['john', 'sarah', 'sam']

# Primeiros convites
print('Saudações, ' + convidados[0].title() + '. Você está convidado para um jantar amanhã.')
print('Saudações, ' + convidados[1].title() + '. Você está convidado para um jantar amanhã.')
print('Saudações, ' + convidados[2].title() + '. Você está convidado para um jantar amanhã.')

# Função sleep em funcionamento
#sleep(1)

# Print mostrando que um convidado não poderia participar mais do jantar
print('Infelizmente, ' + convidados[0].title() + ' não poderá comparecer para o jantar')

# Inserção de nova convidada na lista
convidados[0] = 'adam'

# Print com os novos convites
print('Saudações, ' + convidados[0].title() + '. Você está convidado para um jantar amanhã.')
print('Saudações, ' + convidados[1].title() + '. Você está convidado para um jantar amanhã.')
print('Saudações, ' + convidados[2].title() + '. Você está convidado para um jantar amanhã.')

# Função sleep em funcionamento
#sleep(1)

# Print informando que uma mesa maior foi encontrada
print('Oh céus! Conseguimos uma mesa maior. Por isso, teremos mais convidados para o jantar!')

# Função sleep em funcionamento
#sleep(1)

# Inserção de novos convidados na lista
convidados.insert(0, 'marina')
convidados.insert(2, 'ella')
convidados.append('henry')

# Print dos novos convites
print('Saudações, ' + convidados[0].title() + '. Você está convidado para um jantar amanhã.')
print('Saudações, ' + convidados[1].title() + '. Você está convidado para um jantar amanhã.')
print('Saudações, ' + convidados[2].title() + '. Você está convidado para um jantar amanhã.')
print('Saudações, ' + convidados[3].title() + '. Você está convidado para um jantar amanhã.')
print('Saudações, ' + convidados[4].title() + '. Você está convidado para um jantar amanhã.')
print('Saudações, ' + convidados[5].title() + '. Você está convidado para um jantar amanhã.')

# Função sleep em funcionamento
#sleep(1)

# Contagem de pessoas convidadas para o jantar
print('Para este jantar, foram convidadas {} pessoas.'.format(len(convidados)))