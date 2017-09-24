import urllib2
import urllib
import re
#Cargar pagina
url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = urllib2.urlopen(url)

#Modulos, pendiente.
#code1=urllib.addbase
#code=urllib.addinfourl(code1)

webContent = response.read()

print(webContent[0:300])

#Crear y modificar documento
f = open('obo-t17800628-33.html', 'w') # w sobreescribir
f.write(webContent)
f.close

#Regex
match=re.search(r"^.{10}",webContent,re.S) #importante activar s flag
match2=match.group(0)


#cssselectors and extract
from lxml import cssselect, etree
select=cssselect.CSSSelector("a:contains('Jump to Content')")
root = etree.HTML(webContent)
result=select(root)
result2=result[0].text
print('hello world')


import json
import tools
import tools2
import copy


instruciones1=json.load(open('Instruciones.json'),object_hook=tools._byteify)
instruciones=copy.deepcopy(instruciones1)
resultados={}
linklist="hola"
item=0
flag= False
ins=0
iter=0
first_loop= False
while isinstance(item, int):
    if isinstance(linklist, list):
        if first_loop==True:
            try:
                print("Iteracion :" + str(iter))
                webContent = tools.split_and_load(linklist[iter])
                iter += 1
                first_loop=False
                instruciones2 = copy.deepcopy(instruciones)
            except:
                item = "fail"
                print('First load of loopload fail')
    if ins>=1:
        instruciones["instruciones"].pop(0)
    if instruciones["instruciones"][0]["operation_type"] == "load":
        webContent = tools.split_and_load(instruciones["instruciones"][0]["pagina"])
        link = instruciones["instruciones"][0]["pagina"]
    if instruciones["instruciones"][0]["operation_type"] == "extract":
        resultados[(instruciones["instruciones"][0]["save_var"]+" Evento "+str(iter))] = tools.extract(instruciones["instruciones"][0]["tag"], instruciones["instruciones"][0]["regex"], instruciones["instruciones"][0]["type"], link,webContent)  # Da error porque sigue en la misma instrucion.
    if instruciones["instruciones"][0]["operation_type"] == "loopload": #El nombre de la variable, por cada loop debe ser distinto
        linklist = tools2.loopload(instruciones["instruciones"][0]["tag"], webContent, link)
        first_loop=True
    if instruciones["instruciones"][0]["operation_type"] == "end":
        try:
            print("Iteracion :" + str(iter))
            instruciones = copy.deepcopy(instruciones2)
            webContent = tools.split_and_load(linklist[iter])
            iter += 1
        except:
            item = "fail"
            print('No more iter aviable')



    ins = ins + 1


event=tools.create_dict(resultados)

