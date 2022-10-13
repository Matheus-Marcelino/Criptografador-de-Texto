from string import ascii_lowercase, ascii_uppercase, punctuation, digits
from os import mkdir, path
from shutil import rmtree
from random import choice


def ArquivoINTL():  # apagando a pasta __pycache__
    if path.exists('__pycache__'):
        rmtree('__pycache__')


ArquivoINTL()

letters = [' ', 'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G',
           'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N',
           'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U',
           'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
complexidade = 10


def GerarToken(complexidade=complexidade, caracter=ascii_lowercase + ascii_uppercase + digits):
    token = ''.join(choice(caracter)for _ in range(complexidade))
    return token


def setSave():
    global complexidade

    # escrevendo os digitos e sua criptografia
    def Auxiliar():
        with open('coden/key.txt', 'w') as file:
            file.write(f'complexidade={complexidade}\n')
            for digito in digits:
                file.write(f'{digito}={GerarToken(complexidade)}\n')
            for letra in letters:
                file.write(f'{letra}={GerarToken(complexidade)}\n')
            for symbol in punctuation:
                file.write(f'{symbol}={GerarToken(complexidade)}\n')

    def conjunto():
        file.seek(0, 0)
        file.write(f'complexidade={complexidade}\n')
        for digito in digits:
            file.write(f'{digito}={GerarToken(complexidade)}\n')
        for letra in letters:
            file.write(f'{letra}={GerarToken(complexidade)}\n')
        for symbol in punctuation:
            file.write(f'{symbol}={GerarToken(complexidade)}\n')

    if not path.exists('coden'):
        mkdir('coden')
        Auxiliar()
        with open('coden/read-me.txt', 'w') as aviso:
            aviso.write(
                'Não apague o arquivo "key" ou você perderá a sua criptografia!\n'
                'Caso tenha apagado peça para gerar um novo arquivo, porém a criptografia será outra.\n'
                'dependendo da complexidade que você escolha, pode afetar na velocidade do programa!')
    else:
        try:
            with open('coden/key.txt', 'r+') as file:
                try:
                    temp = file.readline()[13:]
                    file.truncate(0)
                    complexidade = int(temp)
                    if complexidade <= 2:
                        complexidade = 5
                    conjunto()
                except ValueError:
                    complexidade = 10
                    conjunto()
        except FileNotFoundError:
            Auxiliar()
