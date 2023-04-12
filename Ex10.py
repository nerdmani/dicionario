cadastro = {}

while True:
    nome = input('Digite seu nome completo: ')
    if nome == '':
        break
    
    idade = int(input('Digite sua idade: '))
    cidade = input('Digite a Cidade: ')
    
    #Adiciona os dados ao dicionario
    cadastro[nome] = {'idade': idade, 'cidade': cidade}
    
#Imprime o cadatro completo
print('cadastro')
print(cadastro)
for nome, dados in cadastro.items():
    print('-Nome: ', nome)
    print('-Idade: ', dados['idade'])
    print('-Cidade: ', dados['cidade'])
    