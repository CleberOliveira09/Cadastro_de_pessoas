from cadastrar_pessoas.novaPessoa import*
def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'Falha ao criar arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Error ao ler arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())
    finally:
        a.close()


def cadastrar(arq, nome, idade):
    try:
        a = open(arq, 'at')
    except:
        print('Error ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome}: {idade} Anos\n')
        except:
            print('error ao escrever os dados!')
        else:
            print(f'Novo resgisto {nome} cadastrada')





