def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('Error por favor digite um numero inteiro valido')
        else:
            return n



def linha(tam=30):
    return '\033[0;34m-\033[m'*30


def cabeçalho(txt):
    print(linha())
    print(txt.center(30))
    print(linha())


def menu(lista):
    while True:
        c = 1
        for item in lista:
            print(f'\033[0;34m{c} -\033[m \033[0;35m{item}\033[m')
            c += 1
        try:
            r = int(input('\033[0;36mSua Opção:\033[m'))
        except:
            print('comando invalido por favor digite um número valido ')
        else:
            return r





