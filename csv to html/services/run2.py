import csv
# -*- coding: utf-8 -*-
saida = open('final.txt', 'w', encoding="UTF-8")

def countkm(numb):
    if numb==2:
        saida.write(f'<div class="list"><strong>1º REVISÃO</strong>\n')
    if numb == 3:
        saida.write(f'<div class="list"><strong>2º REVISÃO</strong>\n')
    if numb == 4:
        saida.write(f'<div class="list"><strong>3º REVISÃO</strong>\n')
    if numb ==5:
        saida.write(f'<div class="list"><strong>4º REVISÃO</strong>\n')
    if numb == 6:
        saida.write(f'<div class="list"><strong>5º REVISÃO</strong>\n')
    if numb==7:
        saida.write(f'<div class="list"><strong>6º REVISÃO</strong>\n')
    if numb==8:
        saida.write(f'<div class="list"><strong>7º REVISÃO</strong>\n')
    if numb==9:
        saida.write(f'<div class="list"><strong>8º REVISÃO</strong>\n')
    if numb==10:
        saida.write(f'<div class="list"><strong>9º REVISÃO</strong>\n')
    if numb==11:
        saida.write(f'<div class="list"><strong>10º REVISÃO</strong>\n')
    return ''


with open('table3.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0: #Montar o cabeçalho
            saida.write(f'\t<ul class="table__review">\n')
            saida.write(f'\t<li class="table__head">\n')
            line_count += 1
            count=0
            for i in row:
                if count == 0: #pular a primeira info que é vazia
                    count+=1
                else:
                    saida.write(f'\t<div class="list">{i}</div>\n')
            saida.write(f'\t</li>\n')
        else:
            saida.write(f'<li class="table__body" data-carro="{row[1]}">\n')
            saida.write(f'<div class="list">\n<div class="modelo"><h4>{row[1]}</h4></div></div>\n')
            count2=0
            for k in row:
                if count2==0 or count2==1:
                    count2+=1
                    print(count2)
                else:
                    list=countkm(count2)
                    saida.write(f'<div class="valores">{k}</div></div>\n')
                    count2+=1
            saida.write(f'</li>\n')
    saida.write(f'</ul>\n')



