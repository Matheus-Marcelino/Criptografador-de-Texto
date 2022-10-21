from string import ascii_lowercase, ascii_uppercase, punctuation, digits
from os import mkdir, path
from shutil import rmtree
from random import choice


def ArquivoINTL():  # apagando a pasta __pycache__
    if path.exists('__pycache__'):
        rmtree('__pycache__')


ArquivoINTL()

LETTERS = ' AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
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
            for letra in LETTERS:
                file.write(f'{letra}={GerarToken(complexidade)}\n')
            for symbol in punctuation:
                file.write(f'{symbol}={GerarToken(complexidade)}\n')

    def conjunto():
        file.seek(0, 0)
        file.write(f'complexidade={complexidade}\n')
        for digito in digits:
            file.write(f'{digito}={GerarToken(complexidade)}\n')
        for letra in LETTERS:
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


def setCriptografador(barra: str):
    valor = barra.get()
    if valor == '':
        return 'Digite algo na barra a cima :)'
    separador = []
    criptografado = ''

    def main():
        nonlocal criptografado
        with open('coden/key.txt', 'r') as file:
            for letra in valor:
                analisador = len(file.readline()[13:]) - 1
                file.seek(13+analisador, 0)
                for cripto in file:
                    validacao = letra in cripto[:1]
                    if validacao:
                        separador.append(cripto[2:complexidade+2])
                        criptografado = ''.join(separador)
                        break
            return criptografado

    try:
        return main()
    except FileNotFoundError:
        setSave()
        return main()


def setDescriptografador(barra: str):
    valor = barra.get().strip()
    agrupador = []
    separador = descriptografado = ''
    mem, mem2 = 0, complexidade
    # {mem, mem2} usado para avançar pela criptografia no tamanho da complexidade

    def main():
        nonlocal mem, mem2, separador, descriptografado
        with open('coden/key.txt', 'r') as file:
            while True:
                file.seek(0)
                separador = valor[mem:mem2]
                mem += complexidade
                mem2 += complexidade
                if separador != '':
                    for cripto in file:
                        validacao = separador in cripto[2:]
                        if validacao:
                            agrupador.append(cripto[:1])
                            descriptografado = ''.join(agrupador)
                            break
                else:
                    break
            return descriptografado

    try:
        return main()
    except FileNotFoundError:
        setSave()
        return main()


def setOrganizador():  # Apenas quando o programa for iniciado
    global complexidade
    ORGANIZADOR = list()
    if not path.exists('coden'):
        setSave()
        return False

    try:
        with open('coden/key.txt', 'r+') as file:

            def Conjunto():
                file.seek(0)
                len(file.readline()[13:]) - 1

            try:  # primeira ação
                if file.readline()[:13] != 'complexidade=':
                    setSave()
                    ORGANIZADOR.append(True)
                    return ORGANIZADOR

                file.seek(0)
                temp = file.readline()[13:]
                complexidade = int(temp)
                if complexidade <= 2:
                    complexidade = 5
                    setSave()
                    ORGANIZADOR.append(True)
                    return ORGANIZADOR

                if complexidade >= 100:
                    ORGANIZADOR.append(None)

                Conjunto()
                for cripto in file:
                    analisador = len(cripto[2:])-1 != complexidade
                    if analisador:
                        setSave()
                        ORGANIZADOR.append(True)
                        return ORGANIZADOR

                for digit in digits:
                    Conjunto()
                    for inspec in file:
                        analisador = digit in inspec[:1]
                        if analisador:
                            break
                    else:
                        ORGANIZADOR.append(True)
                        return ORGANIZADOR

                for letter in LETTERS:
                    Conjunto()
                    for inspec in file:
                        analisador = letter in inspec[:1]
                        if analisador:
                            break
                    else:
                        ORGANIZADOR.append(True)
                        return ORGANIZADOR

                for punc in punctuation:
                    Conjunto()
                    for inspec in file:
                        analisador = punc in inspec[:1]
                        if analisador:
                            break
                    else:
                        ORGANIZADOR.append(True)
                        return ORGANIZADOR

            except ValueError:
                complexidade = 10
                setSave()
                ORGANIZADOR.append(True)
                return ORGANIZADOR
    except FileNotFoundError:
        setSave()
        ORGANIZADOR.append(True)
        return ORGANIZADOR
    ORGANIZADOR.append(False)
    return ORGANIZADOR
