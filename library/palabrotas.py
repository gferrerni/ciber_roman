import requests


def comprueba_una_palabra(nombre_alumno, palabra):
    url = f"https://www.purgomalum.com/service/json?text={palabra}"

    try:
        r = requests.get(url)
    except:
        print("ERROR: no puedo conectar a [%s]" % url)
        return None

    if r.status_code != 200:
        code = r.status_code

        print(f"ERROR: no existe el recurso [{url}]: {code}")
        return None

    resultado = r.json()
    resultado['nombre_alumno'] = nombre_alumno

    print(resultado)
    return resultado


def comprueba_palabras(nombre_alumno, palabras):
    lista_de_resultados = list()

    for palabra in palabras:
        resultado_llamada = comprueba_una_palabra(nombre_alumno=nombre_alumno, palabra=palabra)
        lista_de_resultados.append(resultado_llamada)
    return lista_de_resultados


def comprueba_solo_frutas(nombre_alumno, palabras):
    FRUTAS = ["apple", "orange", "strawberry", "coconut", "banana"]
    lista_de_resultados = list()

    for palabra in palabras:
        if palabra in FRUTAS:
            resultado_llamada = comprueba_una_palabra(nombre_alumno=nombre_alumno, palabra=palabra)
            lista_de_resultados.append(resultado_llamada)
    return lista_de_resultados
