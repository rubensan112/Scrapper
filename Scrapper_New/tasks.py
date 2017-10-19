import json
import tools
import copy
import step as stepy
import time
aux=[]
def run_step(config, browser):
    for step in config["feed"]["steps"]:
        if step["guid"] == config["guid"]:
            current_step = getattr(stepy, step["class_name"])(config,browser)
            result = current_step.execute(step)
            if step["class_name"] == "LoadPage" or step["class_name"] == "Start":
                browser = result
                config["output_var"] = "Nothing"
            elif step["class_name"] == "Loop":
                config["browser_copy"].append(result[0])
                config["feed_copy"].append(result[1])
            elif step["class_name"] == "End":
                browser = copy.deepcopy(config["browser_copy"][0])
                config["feed"] = copy.deepcopy(config["feed_copy"])
                #Deberia cambiar como se hace esto, y meter segun el numero de iter (dentro de la clase), que se ejecute x veces.( Deberia entrar en la misma instancia de antes, no cambiar)
            else:
                config["output_var"][(step["param"]["save_var"]).split(".")[0]][(step["param"]["save_var"]).split(".")[1]] = result
            config["next_guid"] = step["next_guids"][0]
            config = stepy.del_step(config, config["feed"]["steps"])
            return config["output_var"], config["next_guid"], browser

def run_feed(config):
    browser = None
    for i in range(len(config["feed"]["steps"])):
        if i == 0:
            config["guid"]="ffffffff-ffff-ffff-ffff-ffffffffffff"
        else:
            config["guid"]= config["next_guid"]
        config["output_var"], config["next_guid"], browser = run_step(config, browser)
    return config["next_guid"]

'''
Necesito hacer mas elegante el tema de que entren variables en las clases y funciones. 

Necesito introducir la mecanica del End y iterloops, Extracts

La mecanica del End es sencilla. Cuando empiece un iter, guarda la next_guid y la url como copias, cuando llegue al end, se carga el contenido anterior de la url, y se pasa al next guid

2 cosas pendientes: La primera de ella seria que cada clase devuelva todo, y que entre todo. Asi me ahorro tener que hacer cosas fuera de los pasos.
La otra seria, que la clase loop y loopload se inicialicen solo una vez, asi dentro de cada una de ellas, la variable self, se conservara. Al resto tambien le podria aplicar esto.

Podria empezar inicializando todas las clases con el contenido del feed. (Entonces el self, no tendria informacion informacion cambiante de fuera del paso) Es decir, asi todos los pasos tendrian
unas variables (self) que se irian conservando, y otras que cambiarian cada vez que se ejecuta la clase.

Despues en cada clase, podrian una una inicializacion (del execute) renombrando las variables necesarias (Para una mejor lectura) y al final se anaden al config, o browser, o lo que sea, y el return
devuelve todo.

Tambien podria saltarme la parte de run_feed, ya que realmente lo unico que hace es asignar el primer paso. Le meto como next_guid inicial "ffffffff-ffff-ffff-ffff-ffffffffffff". y ya esta.

'''





config={}
config["feed_copy"] = []
config["browser_copy"] = []
config["start_time"] = time.time()
config["feed"] = json.load(open('feed.json'),object_hook=tools._byteify)
output_var = run_feed(config)



print("--- %s seconds ---" % (time.time() - config["start_time"]))

