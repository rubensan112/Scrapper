import json
import tools
import tools2
import copy
from yapf.yapflib.yapf_api import FormatCode


instruciones1=json.load(open('Instruciones.json'),object_hook=tools._byteify)
instruciones=copy.deepcopy(instruciones1)
resultados=[]
resultadosdict={}
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
        #webContent = tools.split_and_load(instruciones["instruciones"][0]["pagina"])
        webContent = tools.split_and_load1(instruciones["instruciones"][0])
        link = instruciones["instruciones"][0]["pagina"]
    if instruciones["instruciones"][0]["operation_type"] == "extract":
        resultadosdict[instruciones["instruciones"][0]["save_var"]] = tools.extract(instruciones["instruciones"][0]["tag"], instruciones["instruciones"][0]["regex"], instruciones["instruciones"][0]["type"], link,webContent)  # Da error porque sigue en la misma instrucion.
    if instruciones["instruciones"][0]["operation_type"] == "loopload": #El nombre de la variable, por cada loop debe ser distinto
        linklist = tools2.loopload(instruciones["instruciones"][0]["tag"], webContent, link)
        first_loop=True
    if instruciones["instruciones"][0]["operation_type"] == "end":
        try:
            print("Iteracion :" + str(iter))
            instruciones = copy.deepcopy(instruciones2)
            resultados.append(resultadosdict)
            resultadosdict={}
            webContent = tools.split_and_load(linklist[iter])
            iter += 1
        except:
            item = "fail"
            print('No more iter aviable')



    ins = ins + 1


event=tools.create_dict(resultados)



'''
Deberia poner en bonito todo esto, para ver con claridad que hace cada cosa (instruciones["instruciones"][0]["operation_type"]) sustituirlo por algo
Deberia conseguir que el extract tambien extraiga todo lo que haya dentro recursivamente de los nodos.
Deberia quiazas tratar de modular algunas cosas


'''