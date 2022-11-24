import requests

def dime_que_hacer(nombre_alumno):
    url = "https://www.boredapi.com/api/activity"

    try:
        r = requests.get(url)
    except:
        print(f"ERROR: no puedo conectar a {url}")
        return None

    if(r.status_code != 200):
        code = r.status_code
        print(f"ERROR: no encuentro el recursos a {url}: {code}")
        return None

    resultado = r.json()
    resultado['nombre_alumno'] = nombre_alumno

    print(resultado['nombre_alumno']) # John


    return resultado
