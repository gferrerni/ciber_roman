import redis
from dotenv import load_dotenv
from rq import Worker, Queue, Connection

## AQUI CARGAMOS LOS VARIABLES QUE ESTÁN EN EL FICHERO .ENV (PARA NO DEJAR EXPUESTO DATOS SENSIBLES EN GITHUB)
load_dotenv()
PASSWORD = os.getenv('PASSWORD')
PORT = os.getenv('PORT')
HOST = os.getenv('HOST')
REDIS_URL = os.getenv('REDIS_URL')


WORKER_CONN = redis.from_url(REDIS_URL)

REDIS_QUEUES_TO_LISTEN = [
    'cola1'
]

if __name__ == '__main__':
    print(PASSWORD)
    '''
    with Connection(WORKER_CONN):
        worker = Worker(map(Queue, REDIS_QUEUES_TO_LISTEN))
        worker.work()

    '''
