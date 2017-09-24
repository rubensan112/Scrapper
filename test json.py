import json
import tools
import copy
import step as step_py
import time

def run_step(steps,output_var,guid,browser):
    for step in steps:
        if step["guid"] == guid:
            current_step = getattr(step_py, step["class_name"])(aux, output_var)
            result = current_step.execute(step,browser)
            if step["class_name"] == "LoadPage" or step["class_name"] == "Start":
                browser = result
            else:
                output_var[(step["param"]["save_var"]).split(".")[0]][(step["param"]["save_var"]).split(".")[1]] = result
            next_guid = step["next_guids"][0]
            return output_var,next_guid,browser

def run_feed(config):
    browser = None
    for i in range(len(steps)):
        if i == 0:
            guid="ffffffff-ffff-ffff-ffff-ffffffffffff"
        else:
            guid= next_guid
        output_var,next_guid,browser = run_step(steps,output_var,guid,browser)
    return output_var

'''
Necesito hacer mas elegante el tema de que entren variables en las clases y funciones. 

Necesito introducir la mecanica del End y iterloops, Extracts

La mecanica del End es sencilla. Cuando empiece un iter, guarda la next_guid y la url como copias, cuando llegue al end, se carga el contenido anterior de la url, y se pasa al next guid



'''





config={}
config["start_time"] = time.time()
config["feed"] = json.load(open('feed.json'),object_hook=tools._byteify)
config["feed_copy"] = copy.deepcopy(config["feed"])
config["feed_copy"] = copy.deepcopy(config["feed"])
output_var = run_feed(config["feed"]["steps"],config["feed"]["output_var"])



print("--- %s seconds ---" % (time.time() - start_time))

