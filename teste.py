# Thiago Oliveira da Silva
#Algoritmo SmithWaterman de alinhamento de sequências 

import numpy as np
import re 

arquivo = open('input.txt','r')
readArquivo = arquivo.read()
sequencia = re.findall('[A-Z]+', readArquivo)

seq1 = sequencia[0]
seq2 = sequencia[1]

gap = -3
match = 2
missmatch = -1

tamanhoSeq1 = len(seq1)
tamanhoSeq2 = len(seq2)
print(f"Tamanho das sequencias: {tamanhoSeq1}, {tamanhoSeq2}")

matriz = np.zeros((len(seq1) + 1, len(seq2) + 1))
print(matriz)
print(matriz.shape)

for i, linhas in enumerate(matriz):
    for j, elementos in enumerate(linhas):
        if(i==0 and j ==0):
            matriz[i][j] = matriz[i][j-1] +gap
        if(i!=0 and j==0):
            matriz[i][j] = matriz[i-1][j] +gap

for i, linhas in enumerate(matriz):
    for j, elementos in enumerate(linhas):
        # print(f"Acessando -- {i}, {j}")
        if(i == 0 or j == 0): continue
        if i == len(matriz) or j == len(linhas): continue
        if i > len(seq2): continue
        if j > len(seq1): continue
        # print(i, j, len(seq2), len(seq1))
        if seq2[i - 1] == seq1[j - 1]:
            score = match
        else: 
            score = missmatch
        diagonal = matriz[i-1][j-1] + score
        vertical = matriz[i-1][j] + gap
        horizontal = matriz[i][j-1] + gap
        matriz[i][j] = max(diagonal,vertical,horizontal)

tamanhoLinha = len(matriz) -1
tamanhoColuna = len(matriz[0]) -1

sequencia1 = ""
sequencia2 = ""

while tamanhoLinha >= 1:
    print(len(seq1), len(seq2), tamanhoColuna, tamanhoLinha)
    if seq2[tamanhoColuna-1] == seq1[tamanhoLinha-1]:
        sequencia1 += seq2[tamanhoColuna-1]
        sequencia2 += seq2[tamanhoColuna-1]

        tamanhoLinha -=1
        tamanhoColuna -=1

    else:
         
        diagonal = matriz[tamanhoLinha-1][tamanhoColuna-1]
        horizontal = matriz[tamanhoLinha][tamanhoColuna-1]
        vertical = matriz[tamanhoLinha-1][tamanhoColuna]

        if diagonal >= vertical and diagonal >=horizontal:
            sequencia1 += seq1[tamanhoLinha-1]
            sequencia2 += seq2[tamanhoColuna-1]

            tamanhoColuna -=1
            tamanhoLinha -=1
        
        elif horizontal >= diagonal and horizontal >= vertical:
            sequencia1 += '-'
            sequencia2 += seq1[tamanhoColuna-1]

            tamanhoColuna -=1

        elif vertical>= diagonal and vertical >= horizontal:
            sequencia1 += seq2[tamanhoLinha-1]
            sequencia2 += '-'

            tamanhoLinha -=1
        
if tamanhoLinha == 0 and tamanhoColuna >tamanhoLinha:
    sequencia1 += '-'
    sequencia2 += seq1[tamanhoLinha]

sequencia1 = sequencia1[::-1]
sequencia2 = sequencia2[::-1]

# escritas no arquivo output.txt
arquivoSaida = open('output.txt','w')
arquivoSaida.write(str(sequencia1)+'\n')
arquivoSaida.write(str(sequencia2)+'\n')
arquivoSaida.write('SCORE: '+str(matriz[len(matriz) -1][len(matriz[0]) -1]) + '\n')
arquivoSaida.write('GAP: '+ str(gap) + '\n')
arquivoSaida.write('MATCH: ' + str(match) + '\n')
arquivoSaida.write('MISSMATCH: ' + str(missmatch))
arquivoSaida.close()