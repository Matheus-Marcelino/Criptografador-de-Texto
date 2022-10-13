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