from string import ascii_lowercase, ascii_uppercase, punctuation, digits
from os import mkdir, path

LETTERS = ' AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
complexidade = 10


def gerar_token(tamanho=complexidade, caracter=ascii_lowercase + ascii_uppercase + digits) -> str:
    from random import choice
    token = ''.join(choice(caracter)for _ in range(tamanho))
    return token


def save_paste() -> None:
    global complexidade

    # escrevendo os digitos e sua criptografia
    def auxiliar():
        with open('coden/key.txt', 'w', encoding='utf-8') as file:
            file.write(f'complexidade={complexidade}\n')
            for digito in digits:
                file.write(f'{digito}={gerar_token(complexidade)}\n')
            for letra in LETTERS:
                file.write(f'{letra}={gerar_token(complexidade)}\n')
            for symbol in punctuation:
                file.write(f'{symbol}={gerar_token(complexidade)}\n')

    def conjunto():
        file.seek(0, 0)
        file.write(f'complexidade={complexidade}\n')
        for digito in digits:
            file.write(f'{digito}={gerar_token(complexidade)}\n')
        for letra in LETTERS:
            file.write(f'{letra}={gerar_token(complexidade)}\n')
        for symbol in punctuation:
            file.write(f'{symbol}={gerar_token(complexidade)}\n')

    if not path.exists('coden'):
        mkdir('coden')
        auxiliar()
        with open('coden/read-me.txt', 'w', encoding='utf-8') as aviso:
            aviso.write(
                'Não apague o arquivo "key" ou você perderá a sua criptografia!\n'
                'Caso tenha apagado peça para gerar um novo arquivo, porém a criptografia será '
                'outra.\ndependendo da complexidade que você escolha, pode afetar na velocidade '
                'do programa!')
    else:
        try:
            with open('coden/key.txt', 'r+', encoding='utf-8') as file:
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
            auxiliar()


def criptografador(barra: str) -> str:
    valor = barra.get()
    if valor == '':
        return 'Digite algo na barra a cima :)'
    separador = []
    criptografado = ''

    def main():
        nonlocal criptografado
        with open('coden/key.txt', 'r', encoding='utf-8') as file:
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
        save_paste()
        return main()


def descriptografador(barra: str) -> str:
    valor = barra.get().strip()
    agrupador = []
    separador = descriptografado = ''
    mem, mem2 = 0, complexidade
    # {mem, mem2} usado para avançar pela criptografia no tamanho da complexidade

    def main():
        nonlocal mem, mem2, separador, descriptografado
        with open('coden/key.txt', 'r', encoding='utf-8') as file:
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
        save_paste()
        return main()


def setOrganizador() -> list:  # Apenas quando o programa for iniciado
    global complexidade

    ERROR_LIST = [True]
    if not path.exists('coden'):
        save_paste()
        ERROR_LIST.clear()
        ERROR_LIST.append(False)
        return ERROR_LIST

    try:
        with open('coden/key.txt', 'r+', encoding='utf-8') as file:

            def Conjunto():
                file.seek(0)
                len(file.readline()[13:]) - 1

            try:  # primeira ação
                if file.readline()[:13] != 'complexidade=':
                    save_paste()
                    return ERROR_LIST

                file.seek(0)
                temp = file.readline()[13:]
                complexidade = int(temp)
                if complexidade <= 2:
                    complexidade = 5
                    save_paste()
                    return ERROR_LIST

                if complexidade >= 100:
                    ERROR_LIST.append(None)

                Conjunto()
                for cripto in file:
                    analisador = len(cripto[2:])-1 != complexidade
                    if analisador:
                        save_paste()
                        return ERROR_LIST

                for digit in digits:
                    Conjunto()
                    for inspec in file:
                        analisador = digit in inspec[:1]
                        if analisador:
                            break
                    else:
                        save_paste()
                        return ERROR_LIST

                for letter in LETTERS:
                    Conjunto()
                    for inspec in file:
                        analisador = letter in inspec[:1]
                        if analisador:
                            break
                    else:
                        save_paste()
                        return ERROR_LIST

                for punc in punctuation:
                    Conjunto()
                    for inspec in file:
                        analisador = punc in inspec[:1]
                        if analisador:
                            break
                    else:
                        save_paste()

                        return ERROR_LIST

            except ValueError:
                complexidade = 10
                save_paste()
                return ERROR_LIST
    except FileNotFoundError:
        save_paste()
        return ERROR_LIST
    ERROR_LIST.clear()
    ERROR_LIST.append(False)
    return ERROR_LIST


def ArquivoINTL() -> None:  # apagando a pasta __pycache__
    from shutil import rmtree
    if path.exists('__pycache__'):
        rmtree('__pycache__')
