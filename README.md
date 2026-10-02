# Gerador de Senha

Aplicação desktop em Python com interface gráfica (Tkinter) para gerar senhas aleatórias e seguras. Você escolhe os tipos de caracteres e a quantidade, e o programa gera a senha na hora.

## Funcionalidades

- Escolha dos tipos de caracteres da senha:
  - Letras maiúsculas
  - Letras minúsculas
  - Números
  - Caracteres especiais (`!@#$%^&*()-_+=?`)
- Escolha da quantidade de caracteres
- Validação dos dados, com aviso quando:
  - nenhuma opção de caractere está marcada
  - a quantidade está vazia ou é inválida (texto, zero ou negativo)
- Geração segura com o módulo `secrets`, indicado para senhas

## Como usar

1. Marque os tipos de caracteres desejados.
2. Digite a quantidade de caracteres.
3. Clique em **Gerar Senha**.
4. Copie a senha do campo **Senha Gerada**.

## Requisitos

- Python 3.8 ou superior
- tkinter (já vem com o Python no Windows e no macOS)

Não há dependências externas para instalar.

> No Linux, o tkinter pode precisar de instalação: `sudo apt install python3-tk`

## Estrutura do projeto

| Arquivo | Função |
|---|---|
| `main.py` | Ponto de entrada, inicia a interface |
| `interface.py` | Janela e widgets (Tkinter) |
| `logica.py` | Validações, conjunto de caracteres e geração da senha |

## Tecnologias

- Python
- Tkinter
- secrets
- string
