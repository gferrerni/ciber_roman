import requests


def hecho(nombre_alumno, url="https://catfact.ninja/fact"):
    try:
        r = requests.get(url)
    except:
        print("ERROR: no existe el dominio o ha dado error {url}".format(url=url))
        return None
   
    if r.status_code != 200:
        code = r.status_code
        print("ERROR: no puedo conectar a {url}: {code}".format(url=url, code=r.status_code))
        return None

    resultado = r.json()
    resultado['nombre_alumno'] = nombre_alumno

    print(resultado)
    return resultado
