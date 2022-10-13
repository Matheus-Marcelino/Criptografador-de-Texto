from tkinter import DoubleVar, StringVar, TclError, Tk, Label, Button, Entry, Text, PhotoImage, messagebox
from cript import setSave, setCriptografador, setDescriptografador, ArquivoINTL
ArquivoINTL()


def main(ORGANIZADOR=bool()):
    def ComunicadoUrgente():
        if ORGANIZADOR:
            messagebox.showerror(
                'ERROR: 01', 'Ouve Algum problema ou mudança de valor com no arquivo Key,'
                '\nportante ele foi modificado e sua ultima criptografia foi perdida.')
    
    def Aviso():
        aviso = messagebox.askquestion(
            'Save Requestion', 'Ao mudar o save você perderá a sua'
            '\nultima criptografia para sempre.\nDeseja continuar?')
        if aviso == 'yes':
            setSave()
    
    def Display(*args):  # display do criptografador
        caixa = Text(WINDOW_MAIN, height=10, width=30, fg="green")
        caixa.place(x=X/1.98, y=150)
        tamanho = resultado.get()
        if len(tamanho) <= 2000:
            caixa.insert('end', chars=setCriptografador(barra))
        else:
            caixa.insert(
                'end', chars='O limite de 2000 caracteres não pode ser ultrapassado')
    