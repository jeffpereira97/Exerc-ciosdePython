# Importação da lib Sleep
from time import sleep

# Primeira lista de comentários
convidados = ['john', 'sarah', 'sam']

# Primeiros convites
print('Saudações, ' + convidados[0].title() + '. Você está convidado para um jantar amanhã.')
print('Saudações, ' + convidados[1].title() + '. Você está convidado para um jantar amanhã.')
print('Saudações, ' + convidados[2].title() + '. Você está convidado para um jantar amanhã.')

# Função sleep em funcionamento
sleep(1)

# Print mostrando que um convidado não poderia participar mais do jantar
print('Infelizmente, ' + convidados[0].title() + ' não poderá comparecer para o jantar')

# Inserção de nova convidada na lista
convidados[0] = 'adam'

# Print com os novos convites
print('Saudações, ' + convidados[0].title() + '. Você está convidado para um jantar amanhã.')
print('Saudações, ' + convidados[1].title() + '. Você está convidado para um jantar amanhã.')
print('Saudações, ' + convidados[2].title() + '. Você está convidado para um jantar amanhã.')

# Função sleep em funcionamento
sleep(1)

# Print informando que uma mesa maior foi encontrada
print('Oh céus! Conseguimos uma mesa maior. Por isso, teremos mais convidados para o jantar!')

# Função sleep em funcionamento
sleep(1)

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
sleep(1)

# Aviso de que a mesa não chegará a tempo
print('Infelizmente fomos informados que a mesa não chegará a tempo. \nPor isso, teremos que desconvidar algumas pessoas')

# Remoção de convidados via .pop
convidado_1 = convidados.pop()
print('Desculpe pelo inconveniente, ' + convidado_1.title() + ', mas infelizmente terei que desconvidá-lo do jantar')
sleep(1)
convidado_2 = convidados.pop()
print('Desculpe pelo inconveniente, ' + convidado_2.title() + ', mas infelizmente terei que desconvidá-lo do jantar')
convidado_3 = convidados.pop()
print('Desculpe pelo inconveniente, ' + convidado_3.title() + ', mas infelizmente terei que desconvidá-lo do jantar')
convidado_4 = convidados.pop()
print('Desculpe pelo inconveniente, ' + convidado_4.title() + ', mas infelizmente terei que desconvidá-lo do jantar')

# Função sleep em funcionamento
sleep(1)

# Mensagem para mostrar que os restantes na lista ainda estão convidados.
print('Olá, ' + convidados[0].title() + '. Saiba que você ainda está convidado para o jantar.')
print('Olá, ' + convidados[1].title() + '. Saiba que você ainda está convidado para o jantar.')

# Deletando os itens restantes na lista
del convidados[1]
del convidados[0]

# Checando se tudo foi deletado corretamente
print(convidados)