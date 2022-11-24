import resdis
import shodan
form rq import Worker, Queue, Conection

#Importar funciones para poder usarlas
# Por ejemplo from <libreria> import <funcion>

#OJO tenéis que indicar la contraseña, el host y el puerto.
PASSWORD = romaneresuncrack
PORT = 6379
NOSTY = ""


#Hay que modificar esta URL.
REDIS_URL = "redis://redis:6379/"
WORKER_CONN = redis.from_url(REDIS_URL)

SHODAN_APIKEY = "BuOtjrLy1T0t47DuJbBNOWnqmOjlnnFt"
api = shodan.Shodan(SHODAN_APIKEY)

try:
    results = api.search(sys.argv[1])

except shodan.APIError as e:
    print("Error: {}".format(e))

REDIS_QUEUES_TO_LISTEN =[
    'cola3'
]

if __name__ =='main':
    with Conection(WORKER_CONN):
        Worker = Worker(map(Queue, REDIS_QUEUES_TO_LISTEN))
        Worker.WORK()