entrada = open('argo.txt', 'r', encoding="UTF-8")
saida = ''
head = ''
final = open('final.txt', 'w', encoding="UTF-8")
final.write('<!-- versão -->\n<section class="version">\n<div class="heading">')
arq=entrada.readlines()
cont=False
linha=True
a=0
b=False
for i in range(len(arq)):
    teste = arq[i].split()
    if cont == True:
        carro = arq[i].split()
        carro=''.join(carro)
        carro= carro.replace('.','')
        if a!=0:
            saida+='</ul>\n</div>'
        if b == False:
            saida += '<div class="version__choose ' + carro + '">\n<ul>'
            head += '<option class="version__item" data-version= "' + carro + '">' + arq[i] + '</option>\n'
        if b==True:
            saida += '<div class="version__choose ' + carro + ' current">\n<ul>'
            head += '<option class="version__item current" data-version= "' + carro + '">' + arq[i] + '</option>\n'
            b=False

        a+=1
        cont = False
        linha = False
    elif arq[i]=='continue\n':
        cont=True
        linha=False
    elif teste[0] == 'break':
        print(teste)
        print(a)
        if a != 0:
            final.write(head)
            final.write('</select> </div>')
            final.write(saida)
            final.write('</ul>\n</div>')
            final.write('}')
            saida = ''
            head = ''
        head += '\n@@if (context.select === "' + teste[1] + '"){ <h2 class="heading__head">  ESCOLHA A VERSÃO DO SEU ' + \
                teste[1] + '</h2></div>\n'
        head += '<div class="row"> <select class="version__tabs col-sm-8 col-sm-offset-2" id="appearance-select">\n'
        a=0
        linha = False
        cont = True
        b=True
    elif linha==False:
        saida+='<li>'+arq[i]+'</li>\n'

final.write('</section>')