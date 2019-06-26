entrada = open('C:/Users/bianc/Documents/versao.txt', 'r', encoding="UTF-8")
saida = ''
head = ''
final = open('C:/Users/bianc/Documents/final.txt', 'w', encoding="UTF-8")
final.write('<!-- versão -->\n<section class="version">\n<div class="heading">')
arq=entrada.readlines()
cont=False
linha=True
a=0
for i in range(len(arq)):
    teste=arq[i].split()
    if cont == True:
        if a!=0:
            saida+='</ul>\n</div>'
        a+=1
        carro = arq[i].split()
        carro=''.join(carro)
        saida += '<div class="version__choose ' + carro + ' current">\n<ul>'
        head += '<option class="version__item current" data-version= "' + carro + '">' + arq[i] + '</option>\n'
        cont = False
        linha = False
    elif arq[i]=='continue\n':
        cont=True
        linha=False
    elif teste[0] == 'break':
        if i != 0:
            final.write(head)
            final.write('</select> </div>')
            final.write(saida)
            final.write('</ul>')
            final.write('}')
            saida = ''
            head = ''
        head += ' @@if (context.select === "' + teste[1] + '"){ <h2 class="heading__head">  ESCOLHA A VERSÃO DO SEU ' + \
                teste[1] + '</h2></div>\n'
        head += '<div class="row"> <select class="version__tabs col-sm-8 col-sm-offset-2" id="appearance-select">\n'
        linha = False
        cont = True
    elif linha==False:
        saida+='<li>'+arq[i]+'</li>\n'

final.write('</section>')