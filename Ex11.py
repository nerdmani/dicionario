agenda = {}

while True:
    nome = input('Digite o nome da pessoa: ')
    if nome == '':
        break
    
    telefone = input('Digite o Telefone: ')
    
    #adiciona o telefone ao dicionario
    agenda[nome] = telefone
    
#pesquise um telefonena agenda
nome_pesquisa = input('Digite o nome para pesquisar: ')
if nome_pesquisa in agenda:
    print('Telefone de', nome_pesquisa, ':', agenda[nome_pesquisa])

else:
    print('Nome não encontrado na agenda.')