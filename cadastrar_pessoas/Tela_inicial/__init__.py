from cadastrar_pessoas.arquivo import *
from time import sleep
arq = 'arquivo.txt'
if arquivoexiste(arq):
    print('Arquivo encontrado')
else:
    criararquivo(arq)
while True:
    tabela = cabeçalho('\033[0;31mMENU DO SISTEMA\033[m')
    resposta = menu(['pessoas cadastradas','cadastrar pessoas', 'sair do programa'])
    if resposta == 1:
        lerarquivo(arq)
        #Opção de ler arquivo
    elif resposta == 2:
        cabeçalho('Cadastrar pessoa')
        nome = str(input('nome para cadastrar:'))
        idade = leiaint('idade:')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('\033[0;31mSaindo do programa...\033[m')
        sleep(1)
        print('\033[0;31mprograma finalizado!\033[m')
        break
    else:
        print('Error tente novamente')
    sleep(1)
