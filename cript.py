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