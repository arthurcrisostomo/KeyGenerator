
# > Importa tkinter
from tkinter import *

# > Importa a função controller() do logica.py
from logica import controller

def gui():

    # > Instancia a classe Tk para criar a janela principal e armazena na variavel janela
    janela = Tk()

    # > Define o titulo da janela
    janela.title('Gerador de Senha')

    # > Define o tamanho em px da janela
    largura_janela = 500
    altura_janela = 500

    # winfo_screenwidth > Retorna a largura da resolução da tela do usuario
    # winfo_screenheight > Retorna a altura da resolução da tela do usuario
    largura_tela_usuario = janela.winfo_screenwidth()
    altura_tela_usuario = janela.winfo_screenheight()

    """
    largura_tela_usuario // 2 > Divisão Inteira do centro do eixo x(largura da tela)
    altura_tela_usuario // 2 > Divisão Inteira do centro do eixo y(altura da tela)
    largura_janela // 2 > Divisão Inteira do centro do eixo x(largura da janela)
    altura_janela // 2 > Divisão Inteira do centro do eixo y(altura da janela)

    Calculo em resolução de tela 1920x1080 para uma janela tkinter 500x500:
        (960) - (250) = 710 -> (Posição Inicial da janela no eixo x)
        (540) - (250) = 290 -> (Posição Inicial da janela no eixo y)

    Usamos o sinal de -(Subtração) apenas para obter a posição exata (x, y) inicial da janela do programa para que ao abrir sempre comece no meio da tela
    """
    posicao_x = (largura_tela_usuario // 2) - (largura_janela // 2)
    posicao_y = (altura_tela_usuario // 2) - (altura_janela // 2)

    # > Definimos a largura x altura da janela e informamos a posição inicial dele usando (+), o primeiro (+) anuncia o valor de x, o segundo (+) indica o valor de y
    janela.geometry(f'{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}')

    # BooleanVar() > Guarda o valor que o checkbox grava a cada clique, por padrão a variavel recebe False
    estado_maiusculas = BooleanVar()
    estado_minusculas = BooleanVar()
    estado_numeros = BooleanVar()
    estado_caracteres_especiais = BooleanVar()

    ########## FRAME ##########
    # > Cria o frame que contem as checkboxs para definir como vai ser a senha gerada
    frame_opcoes = LabelFrame(
        janela,
        text = 'Opções de Caracteres',
        font = 'Arial 13',
    )
    frame_opcoes.grid(row=0, column=0, padx=(30, 30), pady=(20, 20), sticky='we')

    frame_conteudo = Frame(janela)
    frame_conteudo.grid(row=1, column=0)

    frame_resultado = Frame(janela)
    frame_resultado.grid(row=2, column=0, pady=(100, 0), sticky='we')

    # columnconfigure > Configura qual coluna vai crescer pros lados
    # 0 > Especifica a coluna (coluna do LabelFrame)
    # weight=1 > Define quanto de espaço extra ela recebe
    janela.columnconfigure(0, weight=1)
    frame_resultado.columnconfigure(1, weight=1)

    ########## CHECKBOX ##########
    checkbox_letras_maiusculas = Checkbutton(
        frame_opcoes,
        text = 'Incluir Letras Maiúsculas',
        font = 'Arial 11',
        variable=estado_maiusculas
    )
    checkbox_letras_maiusculas.grid(row=1, column=0, sticky='w')

    checkbox_letras_minusculas = Checkbutton(
        frame_opcoes,
        text = 'Incluir Letras Minúsculas',
        font = 'Arial 11',
        variable=estado_minusculas
    )
    checkbox_letras_minusculas.grid(row=2, column=0, sticky='w')

    checkbox_numeros = Checkbutton(
        frame_opcoes,
        text = 'Incluir Numeros',
        font = 'Arial 11',
        variable=estado_numeros
    )
    checkbox_numeros.grid(row=3, column=0, sticky='w')

    checkbox_caracteres_especiais = Checkbutton(
        frame_opcoes,
        text = 'Incluir Caracteres Especiais',
        font = 'Arial 11',
        variable=estado_caracteres_especiais
    )
    checkbox_caracteres_especiais.grid(row=4, column=0, sticky='w', pady=(0, 100))

    ########## LABEL ##########
    label_qtd_digitos = Label(
        frame_conteudo,
        text = 'Quantidade de Dígitos:',
        font = 'Arial 13'
    )
    label_qtd_digitos.grid(row=1, column=0, sticky='w')

    label_senha_gerada = Label(
        frame_resultado,
        text='Senha Gerada:',
        font='Arial 13'
    )
    label_senha_gerada.grid(row=0, column=0, padx=(5, 0))

    ########## ENTRY ##########
    entry_qtd_caracteres = Entry(
        frame_conteudo,
        font = 'Arial 11',
        width = 4
    )
    entry_qtd_caracteres.grid(row=1, column=1, padx=(5, 0))

    entry_senha_gerada = Entry(
        frame_resultado,
        font='Arial 18'
    )
    entry_senha_gerada.grid(row=0, column=1, sticky='we', padx=(0, 8))

    ########## BUTTON ##########
    button_gerar_senha = Button(
        frame_conteudo,
        text='Gerar Senha',
        font='Arial 13',
        command=lambda: controller(
            estado_maiusculas.get(), estado_minusculas.get(),
            estado_numeros.get(), estado_caracteres_especiais.get(),
            entry_qtd_caracteres.get(), entry_senha_gerada
        )
    )
    button_gerar_senha.grid(row=2, column=0, pady=(30, 0))

    # > Deixa a janela em loop para ficar sempre aberta
    janela.mainloop()