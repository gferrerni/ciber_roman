import os
import time
import library
import threading
from rq import Queue
from redis import Redis
from dotenv import load_dotenv

## AQUI CARGAMOS LOS VARIABLES QUE ESTÁN EN EL FICHERO .ENV (PARA NO DEJAR EXPUESTO DATOS SENSIBLES EN GITHUB)
load_dotenv()
PASSWORD = os.getenv('PASSWORD')
PORT = os.getenv('PORT')
HOST = os.getenv('HOST')
REDIS_URL = os.getenv('REDIS_URL')
REDIS_PORT = os.getenv('REDIS_PORT')
ntp = int(round(time.time() * 1000))

redis_conn = Redis(host='redis',port=REDIS_PORT) 
q = Queue('COLA_ATP_GF', connection=redis_conn)

def cola(tarea_actual):
        print(f'Empezando tarea:{tarea_actual}')
        q.enqueue(tarea_actual)
        time.sleep(1)
        print("Tarea completada")
        q.pop(tarea_actual)


if __name__ == '__main__':
    tareas = [library.aburrimiento.dime_que_hacer("ATP"),library.gatos.hecho("ATP"),library.palabrotas.comprueba_una_palabra("ATP",["mierda","puta"])]

    for tarea_actual in tareas:
    	cola(tarea_actual)
    	

