from tkinter import DoubleVar, StringVar, TclError, Tk, Label, Button, Entry, Text, PhotoImage, messagebox
from cript import save_paste, criptografador, descriptografador


def main(message: list) -> None:
    def comunicado_urgente() -> None:
        if message[0] is True:
            messagebox.showwarning('Aviso Importante', 'A sua complexidade está acima de 100\n'
                                   'Problemas de performance podem aparecer.')

        try:
            if message[0] is None or message[1] is None:
                messagebox.showerror(
                    'ERROR: 01', 'Ouve Algum problema ou mudança de valor no arquivo Key,'
                    '\nportante ele foi modificado e sua ultima criptografia foi perdida.')
        except IndexError:
            pass

    def aviso() -> None:
        aviso = messagebox.askquestion(
            'Save Requestion', 'Ao mudar o save você perderá a sua'
            '\nultima criptografia para sempre.\nDeseja continuar?')
        if aviso == 'yes':
            save_paste()

    def display(*args) -> None:  # display do criptografador
        caixa = Text(WINDOW_MAIN, height=10, width=30, fg="green")
        caixa.place(x=X/1.98, y=150)
        tamanho = resultado.get()
        if len(tamanho) <= 2000:
            caixa.insert('end', chars=criptografador(barra))
        else:
            caixa.insert(
                'end', chars='O limite de 2000 caracteres\nnão pode ser ultrapassado')
            resultado.set(tamanho[0:2000])
            tamanho_final.set(2000)

    def display_2(*args) -> None:  # display do descriptografador
        caixa = Text(WINDOW_MAIN, height=10, width=30, fg="green")
        caixa.place(x=X/5.2, y=150)
        tamanho = resultado.get()
        if len(tamanho) <= 20000:
            caixa.insert('end', chars=descriptografador(barra))

    def responsividade() -> None:  # Responsividade do contador
        lendo = int(tamanho_final.get())
        lendo = len(str(lendo))

        if lendo == 1:
            identificador_descrip.place(x=X/2.87, y=50)
            identificador2_crip.place(x=X/1.72, y=50)
        elif lendo == 2:
            identificador_descrip.place(x=X/2.9, y=50)
            identificador2_crip.place(x=X/1.71, y=50)
        elif lendo == 3:
            identificador_descrip.place(x=X/2.97, y=50)
            identificador2_crip.place(x=X/1.69, y=50)
        elif lendo == 4:
            identificador_descrip.place(x=X/3.04, y=50)
            identificador2_crip.place(x=X/1.67, y=50)
        elif lendo == 5:
            identificador_descrip.place(x=X/3.11, y=50)
            identificador2_crip.place(x=X/1.65, y=50)

    def contador() -> None:  # Conta o número de caracteres
        tamanho = len(resultado.get())
        tamanho_final.set(0) \
            if tamanho == 0 else tamanho_final.set(tamanho)

    def limpar() -> None:
        barra.delete(0, 'end')
        display()
        display_2()
        tamanho_final.set(0)
        identificador_crip['fg'] = identificador2_crip['fg'] = \
            identificador_descrip['fg'] = identificador2_descrip['fg'] = "green"
        responsividade()

    def limitador(*args) -> None:
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

    def atualizador(*args) -> None:
        contador()
        responsividade()

    try:
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
            WINDOW_MAIN.destroy()

        # nome do programa
        Label(WINDOW_MAIN, text="JOSH", bg="black",
              fg="green", anchor='n').place(x=X/2.1, y=0.2)

        # aviso
        comunicado_urgente()

        Label(WINDOW_MAIN, text="AVISO", bg="black", font="Arial 13",
              fg="red", anchor='n').place(x=X/2.15, y=90)
        Label(WINDOW_MAIN, text="CARACTERES ACENTUADOS NÃO SERÃO LIDOS!", bg="black",
              font="Arial 10", fg="green", anchor='n').place(x=X/3.13, y=117)

        # footer
        Label(WINDOW_MAIN, text="O programa ainda está em desenvolvimento,"
              "podendo ter problemas de performance.\nSempre que "
              "puder apague os textos dentro das caixas, oque ajuda bastante no desempenho\n"
              "e de preferência não coloque frases gigantes para serem criptografadas.\n "
              "Obrigado por usar o programa!",
              bg="black", fg="green", font="Arial 9", anchor='w').place(x=X/5.5, y=320)

        # barra de escrita, seu limitador e seu vizualizador
        # coletando os dados da barra, definindo o len() e o tamanho maximo
        resultado, tamanho_final = StringVar(), DoubleVar()
        resultado.trace('w', limitador)
        tamanho_final.set(0)

        barra = Entry(WINDOW_MAIN, fg="green",
                      textvariable=resultado, width=31)
        barra.place(x=X/2.7, y=21, width=218)
        barra.bind("<KeyRelease>", atualizador)  # detector do teclado

        # configurando a variavel em seus locais
        identificador_crip = Label(WINDOW_MAIN, bg='black', fg="green",
                                   anchor='n', textvariable=tamanho_final)
        identificador_crip.place(x=X/1.77, y=50)
        identificador2_crip = Label(
            WINDOW_MAIN, text='/ 2000', bg='black', fg="green", anchor='n')
        identificador2_crip.place(x=X/1.72, y=50)

        identificador_descrip = Label(
            WINDOW_MAIN, bg='black', fg="green", anchor='n', textvariable=tamanho_final)
        identificador_descrip.place(x=X/2.87, y=50)
        identificador2_descrip = Label(
            WINDOW_MAIN, text='/ 20000', bg='black', fg="green", anchor='n')
        identificador2_descrip.place(x=X/2.75, y=50)

        # displays e associados
        Label(text=display())
        Label(text=display_2())

        Button(WINDOW_MAIN, text="Save", command=lambda: aviso(),
               width=4).place(x=X/2, y=50, height=19)

        Button(WINDOW_MAIN, text="Criptografar", command=display).place(
            x=X/1.544, y=21, height=19)

        Button(WINDOW_MAIN, text="Descriptografar",
               command=display_2).place(x=X/4, y=21, height=19)

        Button(WINDOW_MAIN, text='Limpar', command=limpar).place(
            x=X/2.3, y=50, height=19)

        WINDOW_MAIN.mainloop()
    except TclError:
        pass
