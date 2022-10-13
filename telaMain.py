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

    def Display2(*args):  # display do descriptografador
        caixa = Text(WINDOW_MAIN, height=10, width=30, fg="green")
        caixa.place(x=X/5.2, y=150)
        tamanho = resultado.get()
        if len(tamanho) <= 20000:
            caixa.insert('end', chars=setDescriptografador(barra))
        else:
            return ''

    def Limpar():
        barra.delete(0, 'end')
        Display()
        Display2()
        tamanho_final.set(0.0)
        identificador_crip['fg'] = identificador2_crip['fg'] = \
            identificador_descrip['fg'] = identificador2_descrip['fg'] = "green"

    def Limitador(*args):
        tamanho = resultado.get()
        if len(tamanho) >= 5500:
            identificador_descrip['fg'] = identificador2_descrip['fg'] = "yellow"
            if len(tamanho) >= 8000:
                identificador_descrip['fg'] = identificador2_descrip['fg'] = "red"
                resultado.set(tamanho[0:20000])
        else:
            identificador_descrip['fg'] = identificador2_descrip['fg'] = "green"

        if len(tamanho) > 2000:
            identificador_crip['fg'] = identificador2_crip['fg'] = "red"
        else:
            identificador_crip['fg'] = identificador2_crip['fg'] = "green"

    def CaracterCont(*args):
        tamanho = len(resultado.get())
        tamanho_final.set(0.0) if tamanho == 0 else tamanho_final.set(tamanho)

    X, Y = int(800), int(400)
    WINDOW_MAIN = Tk()
    WINDOW_MAIN.resizable(width=False, height=False)
    WINDOW_MAIN.title("Criptografador")
    WINDOW_MAIN.geometry(f"{X}x{Y}+300+200")
    WINDOW_MAIN["bg"] = "black"
    try:
        WINDOW_MAIN.call('wm', 'iconphoto', WINDOW_MAIN._w,
                         PhotoImage(file='icon/key.png'))
    except TclError:
        messagebox.showerror(
            title='ERROR: 02', message='A pasta icon foi excluida ou algum arquivo'
            ' modificado,\nPorfavor reinstale o aplicativo')
        pass
    
    # nome do programa
    Label(WINDOW_MAIN, text="JOSH", bg="black",
          fg="green", anchor='n').place(x=X/2.1, y=0.2)

    # aviso
    ComunicadoUrgente()
    
    
    Label(WINDOW_MAIN, text="AVISO", bg="black", font="Arial 13",
          fg="red", anchor='n').place(x=X/2.15, y=90)
    Label(WINDOW_MAIN, text="CARACTERES ACENTUADOS NÃO SERÃO LIDOS!", bg="black", font="Arial 10",
          fg="green", anchor='n').place(x=X/3.13, y=117)

    # footer
    Label(WINDOW_MAIN, text="O programa ainda está em desenvolvimento, podendo ter problemas de performance.\n"
          "Sempre que puder apague os textos dentro das caixas, oque ajuda bastante no desempenho\n"
          "e de preferência não coloque frases gigantes para serem criptografadas.\n "
          "Obrigado por usar o programa!",
          bg="black", fg="green", font="Arial 9", anchor='w').place(x=X/5.5, y=320)

    # barra de escrita, seu limitador e seu vizualizador
    # coletando os dados da barra, definindo o len() e o tamanho maximo
    resultado, tamanho_final = StringVar(), DoubleVar()
    resultado.trace('w', Limitador)

    
    WINDOW_MAIN.mainloop()