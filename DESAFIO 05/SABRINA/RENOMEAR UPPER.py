import os
import tkinter as tk
from tkinter import filedialog

def renomear_arquivos(diretorio):
    try:
        # Lista todos os arquivos no diretório selecionado
        arquivos = os.listdir(diretorio)

        # Para cada arquivo no diretório
        for arquivo in arquivos:
            # Verifica se o arquivo é um arquivo regular (não é um diretório)
            if os.path.isfile(os.path.join(diretorio, arquivo)):
                # Separa o nome do arquivo e a extensão
                nome_arquivo, extensao = os.path.splitext(arquivo)

                # Remove espaços e renomeia o arquivo para maiúsculas
                nome_arquivo_upper = nome_arquivo.replace(" ", "_").upper()
                novo_nome = f"{nome_arquivo_upper}{extensao}"
                os.rename(os.path.join(diretorio, arquivo), os.path.join(diretorio, novo_nome))

        mensagem.config(text="Arquivos renomeados com sucesso para maiúsculas!")

    except Exception as e:
        mensagem.config(text=f"Ocorreu um erro: {str(e)}")

def selecionar_diretorio():
    diretorio = filedialog.askdirectory()
    if diretorio:
        renomear_arquivos(diretorio)

# Cria a janela principal
janela = tk.Tk()
janela.title("Renomear Arquivos para Maiúsculas")

# Cria um botão para selecionar o diretório
selecionar_botao = tk.Button(janela, text="Selecionar Diretório", command=selecionar_diretorio)
selecionar_botao.pack(pady=20)

# Cria uma área para exibir mensagens
mensagem = tk.Label(janela, text="", fg="green")
mensagem.pack()

# Inicia a interface gráfica
janela.mainloop()
