from string import ascii_lowercase, ascii_uppercase, punctuation, digits
from os import mkdir, path
from shutil import rmtree
from random import choice


def ArquivoINTL():  # apagando a pasta __pycache__
    if path.exists('__pycache__'):
        rmtree('__pycache__')


ArquivoINTL()


