import redis
from rq import Worker, Queue, Connection

# Importar funciones para poder usarlas
# Por ejemplo from <libreria>.<fichero> import <funcion>

# OJO que tenéis que indicar la contraseña, el host y el puerto.
PASSWORD = "FWflewhfwlehfwoihf204X7234fwef"
PORT = 30000
HOST = "tintagel.0z0ne.com"

# Hay que modificar esta URL.
REDIS_URL = "redis://redis:6379/"
WORKER_CONN = redis.from_url(REDIS_URL)

REDIS_QUEUES_TO_LISTEN = [
    'cola1'
]

if __name__ == '__main__':
    with Connection(WORKER_CONN):
        worker = Worker(map(Queue, REDIS_QUEUES_TO_LISTEN))
        worker.work()
