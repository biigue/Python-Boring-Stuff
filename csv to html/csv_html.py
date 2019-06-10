import csv
# -*- coding: utf-8 -*-
tabela = open('tabela.txt', 'w', encoding="UTF-8")
nome = open('nome.txt', 'w', encoding="UTF-8")
nome.write(f'\t<tr><td></td></tr>\n')

def mes(contador):
    if contador==0:
        colunas=7
    else:
        colunas=6
    for i in range(colunas):
        if i ==0 and colunas==7:
            nome.write(f'\t<tr><td>{row[contador + i]}</td></tr>\n')
        else:
            tabela.write(f'\t<td>{row[contador + i]}</td>\n')
    return contador+colunas

with open('clubinho.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0: #pular a primeira linha
            line_count += 1

        else:
            #Estrutura Mês > Créditos - Pontos - Cotas - Extra - Extra - Total
            contador = 0
            tabela.write(f'\t<tr>\n')
            tabela.write('<!-- Janeiro -->\n')
            contador= mes(contador)
            tabela.write('<!-- Fevereiro -->\n')
            contador = mes(contador)
            tabela.write('<!-- Março -->\n')
            contador = mes(contador)
            tabela.write('<!-- Abril -->\n')
            contador = mes(contador)
            tabela.write('<!-- Maio -->\n')
            contador = mes(contador)
            tabela.write('<!-- Total -->\n')
            contador = mes(73)
            tabela.write(f'\t</tr>\n')
            line_count += 1