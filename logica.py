
# > Importa a costante END e Importa submodulo messagebox para exibir pop-up
from tkinter import END, messagebox

# > Importa secrets para sortear elementos de uma sequencia
import secrets

# > Importa biblioteca string para manipular letras, numeros e simbolos
import string

def controller(maiusculas, minusculas, numeros, caracteres, qtd_caracteres, entry_senha_gerada):

    # > Chama a função responsável por validar os checkboxs e retorna o resultado para validacao_checkbox
    validacao_checkbox = validar_checkbox(maiusculas, minusculas, numeros, caracteres)

    # > Caso validacao_checkbox seja False encerra o controller sem gerar a senha
    if not validacao_checkbox:
        return

    # > Chama a função responsável por validar o tipo de dado inserido no entry que informa a quantidade de caracteres que a senha deve ter e retorna o resultado para validacao_qtd_digitos
    validacao_qtd_digitos = validar_qtd_caracteres(qtd_caracteres)

    # > Caso validacao_qtd_digitos seja False encerra o controller sem gerar a senha
    if not validacao_qtd_digitos:
        return

    # > Chama a função responsavel por gerar o conjunto de caracteres com base nas escolhas do checkbox
    conjunto_caracteres = montar_conjunto_caracteres(maiusculas, minusculas, numeros, caracteres)

    # > Chama a função responsavel por sortear/gerar a senha e passa pra ela a quantidade de caracteres que a senha deve conter
    senha_gerada = sortear_senha(conjunto_caracteres, qtd_caracteres)

    # > Chama a função responsavel por exibir a senha gerada no entry_senha_gerada que passamos para ela
    exibir_senha(senha_gerada, entry_senha_gerada)

def validar_checkbox(checkbox1, checkbox2, checkbox3, checkbox4):

    # > Verifica se todos os chackboxs estão desmarcados
    if not checkbox1 and not checkbox2 and not checkbox3 and not checkbox4:

        # > Exibe um pop-up
        messagebox.showwarning('Aviso', 'Nenhuma opção selecionada. Tente Novamente!')

        # > Retorna False para quem chamou a função
        return False

    # > Retorna True caso esteja no minimo 1 checkbox marcado
    return True

def validar_qtd_caracteres(qtd_caracteres):

    # > Verifica se o valor inserido esta vazio
    if qtd_caracteres.strip() == '':
        messagebox.showwarning('Aviso', 'Por favor, informe a quantidade de caracteres que a senha deve ter!')

        return False

    # > Verifica se o valor inserido é um numero ou se é menor que 1
    if not qtd_caracteres.isdigit() or int(qtd_caracteres) < 1:
        messagebox.showwarning('Aviso', 'Por favor, insira um valor válido para a quantidade de caracteres!')
        return False

    return True

def montar_conjunto_caracteres(maiusculas, minusculas, numeros, caracteres):

    conjunto = ''

    # > Verifica e vai adicionando a variavel conjunto os caracteres com base nos checkboxs marcados
    if maiusculas:
        conjunto += string.ascii_uppercase
    if minusculas:
        conjunto += string.ascii_lowercase
    if numeros:
        conjunto += string.digits
    if caracteres:
        conjunto += '!@#$%^&*()-_+=?'

    # > Retorna o conjunto para quem chamou a função
    return conjunto

def sortear_senha(conjunto_caracteres, qtd_caracteres):

    # > Utilizando For Comprehension para gerar a senha de forma aleatoria de acordo com a quantidade de digitos que o usuario escolheu
    senha_gerada = ''.join(secrets.choice(conjunto_caracteres) for _ in range(int(qtd_caracteres)))

    # > Retorna a senha gerada pra quem a chamou
    return senha_gerada

def exibir_senha(senha_gerada, entry_senha_gerada):
    # > Deleta o texto atual que esta no entry
    entry_senha_gerada.delete(0, END)

    # > Adiciona a senha gerada no entry_senha_gerada
    entry_senha_gerada.insert(0, senha_gerada)