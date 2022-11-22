import os
import csv
# -*- coding: utf-8 -*-
pt = open('trads/pt.json', 'w')
es = open('trads/es.json', 'w')
en = open('trads/en.json', 'w')


def endof():
    pt.write('},\n')
    es.write('},\n')
    en.write('},\n')


def setAll(val):
    pt.write(f'\t"{val}": ')
    pt.write('{\n')
    es.write(f'\t"{val}": ')
    es.write('{\n')
    en.write(f'\t"{val}": ')
    en.write('{\n')


with open('c:\\Users\\bianc\\Pictures\\Python-Boring-Stuff\\trads\\entrada.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            pt.write('{\n')
            es.write('{\n')
            en.write('{\n')
            line_count += 1
        else:
            if row[1] == '' and row[2] == '':
                setAll(row[0])
            else:
                pt.write(f'\t"{row[0]}": "{row[1]}",\n')
                en.write(f'\t"{row[0]}": "{row[2]}",\n')
                es.write(f'\t"{row[0]}": "{row[3]}",\n')
# pt.write(f'</ul>\n')
# es.write(f'</ul>\n')
# en.write(f'</ul>\n')
endof()
pt.close
en.close
es.close


# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

# f = open("trads/pt.json", "w")
# f.write("\nSee you soon!x")
# f.close()
