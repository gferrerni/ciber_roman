from rq import Queue
from redis import Redis

# Importar funciones para poder usarlas
# Por ejemplo from <libreria>.<fichero> import <funcion>


if __name__ == '__main__':
    # OJO que tenéis que indicar la contraseña, el host y el puerto.
    PASSWORD = "Ffwsefhkw2222222jfhwekfew3333333we"
    PORT = 30000
    HOST = "tintagel.0z0ne.com"

    redis_conn = Redis(
        host='redis',
        port=6379) 
    
    q = Queue('cola1', connection=redis_conn)
    job = q.enqueue(
    #    <libreria>.<fichero>.<funcion>
    # Añadir parametros si son necesarios
    # ...
    )
