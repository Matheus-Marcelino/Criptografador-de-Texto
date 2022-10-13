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


WINDOW_LOADING = Tk()
WINDOW_LOADING.resizable(width=False, height=False)
WINDOW_LOADING.title("Criptografador -- Loading")
WINDOW_LOADING.geometry("500x200+500+300")
WINDOW_LOADING["bg"] = "black"
try:
    WINDOW_LOADING.call('wm', 'iconphoto', WINDOW_LOADING._w,
                        PhotoImage(file='icon/key.png'))
except TclError:
    messagebox.showerror(
        title='ERROR: 02', message='A pasta "icon" foi excluida ou algum arquivo modificado,'
        '\nPorfavor reinstale o Programa')
    pass

Label(WINDOW_LOADING, text='Loading...', fg='green',
      bg='black', font="Bahnschrift 15").place(x=85, y=70)

for i in range(16):  # Criando os primeios quadrados
    Label(WINDOW_LOADING, bg='black', width=2,
          height=1).place(x=(i+4)*22, y=100)

WINDOW_LOADING.update()
ORGANIZADOR = animacao()
WINDOW_LOADING.mainloop()
main(ORGANIZADOR)
