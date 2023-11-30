# Universidade Federal do Piauí
# Centro de Ciências da Natureza
# Departamento de Computação
# Prof. Dr. Luiz Claudio Demes da Mata Sousa
# Aluno(a): Bianca Bastos de Souza
# Atividade 02 - Ribossomo: Criando um ribossomo
# Obs: Numero do Aluno = 5 

import pandas as pd
import tkinter as tk
from tkinter import filedialog


#metodo que le uma celula especifica de uma planilha xlsx 
def ler_celula1():
    nome_arq_xlsx = '4.Atividade.Anexo.Ribossomo.xlsx'
    nome_planilha = 'RNA.sequencias'
    numero_aluno = int(linha_entry.get()) - 1
    nome_coluna = 'RNA'

    try:
        df = pd.read_excel(nome_arq_xlsx, sheet_name=nome_planilha)
        valor_celula = df.at[numero_aluno, nome_coluna]
        traducao(valor_celula)  # Chama o método que realiza a tradução
        resultado.config(text=f"Resultado: Tradução concluída")
    except Exception as e:
        resultado.config(text=f"Ocorreu um erro: {e}")


def ler_celula(aluno_numero, disciplina_selecionada):
    # aluno_numero = linha_entry.get()
    # disciplina_selecionada = disciplina_var.get()

    # Comportamento baseado na opção selecionada
    if disciplina_selecionada == "Biologia":
        # Lógica específica para a disciplina de Biologia
        resultado["text"] = "Resultado para Aluno {} na disciplina de Biologia".format(aluno_numero)
    elif disciplina_selecionada == "Bioinformática":
        # Lógica específica para a disciplina de Bioinformática
        resultado["text"] = "Resultado para Aluno {} na disciplina de Bioinformática".format(aluno_numero)
    else:
        resultado["text"] = "Selecione uma disciplina antes de executar."

#metodo que traduz as bases RNA em proteinas num arquivo txt
def traducao(string):
    start = "AUG"
    # Tamanho do bloco
    tamanho_bloco = 3

    # Loop para percorrer a string de 3 em 3 caracteres
    for i in range(0, len(string) - tamanho_bloco + 1, tamanho_bloco):
        bloco = string[i:i + tamanho_bloco]
        if bloco == start:
            string2 = string[i:]
            traducao2(string2)
            return
        
    #caso não haja start
    nome_arquivo_txt_destino = 'aminoacidos.txt'
    with open(nome_arquivo_txt_destino, 'w', encoding='utf-8') as arquivo_txt:
        arquivo_txt.write("Nenhum aminoacido foi produzido!")
            

def traducao2(string):
    dicionario = {
    'AUG': 'MET(START)',
    'UAA': 'OCRE(STOP)', 'UAG': 'AMBAR(STOP)', 'UGA': 'OPALA(STOP)',
    'UUU':'FENIL', 'UUC': 'FENIL', 
    'UUA': 'LEUC', 'UUG': 'LEUC', 'CUU': 'LEUC', 'CUC': 'LEUC', 'CUA': 'LEUC', 'CUG': 'LEUC',
    'AUU': 'ISO', 'AUC': 'ISO', 'AUA': 'ISO', 
    'GUU': 'VAL', 'GUC': 'VAL', 'GUA': 'VAL', 'GUG': 'VAL',
    'UCU': 'SER', 'UCC': 'SER', 'UCA': 'SER', 'UCG': 'SER',
    'CCU': 'PROL', 'CCC': 'PROL', 'CCA': 'PROL', 'CCG': 'PROL',
    'ACU': 'TREO', 'ACC': 'TREO', 'ACA': 'TREO', 'ACG': 'TREO',
    'GCU': 'ALA', 'GCC': 'ALA', 'GCA': 'ALA', 'GCG': 'ALA', 
    'UAU': 'TIRO', 'UAC': 'TIRO',
    'CAU': 'HISTI', 'CAC': 'HISTI',
    'GLUT': 'CAA', 'CAG': 'GLUT',
    'AAU': 'ASPAR', 'AAC': 'ASPAR',
    'AAA': 'LIS', 'AAG': 'LIS',
    'GAU': 'Ac.ASPART', 'GAC': 'Ac.ASPART', 'GAA': 'Ac.GLUT', 'GAG': 'Ac.GLUT',
    'UGU': 'CIST', 'UGC': 'CIST', 
    'UGG': 'TRIP', 
    'CGU': 'ARGIN', 'CGC': 'ARGIN', 'CGA': 'ARGIN', 'CGG': 'ARGIN','AGA': 'ARGIN', 'AGG': 'ARGIN',
    'AGU': 'SER', 'AGC': 'SER', 
    'GGU': 'GLIC', 'GGC': 'GLIC', 'GGA': 'GLIC', 'GGG': 'GLIC'
}
    # Tamanho do bloco
    tamanho_bloco = 3
    nome_arquivo_txt_destino = 'aminoacidos.txt'

    # Loop para percorrer a string de 3 em 3 caracteres
    with open(nome_arquivo_txt_destino, 'w', encoding='utf-8') as arquivo_txt:
        for i in range(0, len(string) - tamanho_bloco + 1, tamanho_bloco):
            bloco = string[i:i + tamanho_bloco]
            if bloco in dicionario:
                arquivo_txt.write(dicionario[bloco])
                if i + tamanho_bloco < len(string):
                    arquivo_txt.write("--")
                if bloco == "UAA" or  bloco == "UAG" or bloco == "UGA":
                    break                

# Configuração da janela principal
root = tk.Tk()
root.title("Smith Waterman Algorithm: ")

# Rótulos e botoes
# Botões de seleção para escolher a disciplina
disciplina_var = tk.StringVar()
disciplina_var.set("Biologia")  # Define Biologia como a opção padrão

bio_button = tk.Radiobutton(root, text="Biologia", variable=disciplina_var, value="Biologia")
bio_button.pack()

bioinfo_button = tk.Radiobutton(root, text="Bioinformática", variable=disciplina_var, value="Bioinformática")
bioinfo_button.pack()

#leitura linha
linha = tk.Label(root, text="Número do Aluno:")
linha.pack()
linha_entry = tk.Entry(root)
linha_entry.pack()


# Botão para executar a tradução
transc_button = tk.Button(root, text="Executar Tradução", command=lambda:ler_celula(linha_entry.get(), disciplina_var.get()))
transc_button.pack()

# Rótulo para exibir o resultado
resultado = tk.Label(root, text="")
resultado.pack()


root.mainloop()






