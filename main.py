from tkinter import TclError, Tk, Label, PhotoImage, messagebox
from cript import setOrganizador
from telaMain import main
from time import sleep


def animacao():
    try:
        for _ in range(5):  # quanto vai demorar
            for j in range(16):  # quantidade de quadrados
                # colorindo de verde
                Label(WINDOW_LOADING, bg='#00c900',
                      width=2, height=1).place(x=(j+4)*22, y=100)
                sleep(0.06)
                WINDOW_LOADING.update_idletasks()

                # colorindo de preto
                Label(WINDOW_LOADING, bg='#1F2732',
                      width=2, height=1).place(x=(j+4)*22, y=100)
        ORGANIZADOR = setOrganizador()
        WINDOW_LOADING.destroy()
        return ORGANIZADOR
    except TclError:
        pass
