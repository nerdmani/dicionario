dicionario = {'gato':'chat',
'cachorro': 'chien',
'cavalo' : 'cheval'}

palavras = ['gato', 'lion', 'cavalo']

for palavra in palavras:
    if palavra in dicionario:
        print(palavra, '->', dicionario [palavra])
    else:
        print(palavra, '-> não esta no dicionario')