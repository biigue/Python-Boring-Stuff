import os
import csv
# -*- coding: utf-8 -*-
pt = open('trads/pt.json', 'w')
es = open('trads/es.json', 'w')
en = open('trads/en.json', 'w')

file = open('trads/entrada.csv', 'r')
items = file.readlines()


def setAll(val):
    pt.write(f'\t"{val}": ')
    pt.write('{\n')
    es.write(f'\t"{val}": ')
    es.write('{\n')
    en.write(f'\t"{val}": ')
    en.write('{\n')


def endof():
    pt.write('}\n')
    es.write('}\n')
    en.write('}\n')


for i in range(0, len(items)):
    if i > 0:
        text = items[i].replace('\n', '').split(',')
        if text[1] == '' and text[2] == '':
            if i > 1:
                pt.write('},\n')
                es.write('},\n')
                en.write('},\n')
            setAll(text[0])
        else:
            try:
                next = items[i+1].replace('\n', '').split(',')
                if next[1] == '' and next[2] == '':
                    pt.write(f'\t"{text[0]}": "{text[1]}"\n')
                    en.write(f'\t"{text[0]}": "{text[2]}"\n')
                    es.write(f'\t"{text[0]}": "{text[3]}"\n')
                else:
                    pt.write(f'\t"{text[0]}": "{text[1]}",\n')
                    en.write(f'\t"{text[0]}": "{text[2]}",\n')
                    es.write(f'\t"{text[0]}": "{text[3]}",\n')
            except:
                pt.write(f'\t"{text[0]}": "{text[1]}"\n')
                en.write(f'\t"{text[0]}": "{text[2]}"\n')
                es.write(f'\t"{text[0]}": "{text[3]}"\n')
                endof()
    else:
        pt.write('{\n')
        es.write('{\n')
        en.write('{\n')
endof()

pt.close
en.close
es.close
