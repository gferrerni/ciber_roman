import sys

from libreria.gatos import hecho
from libreria.palabrotas import comprueba_palabras, comprueba_solo_frutas
from libreria.aburrimiento import dime_que_hacer


resultado = hecho(nombre_alumno="Román")

resultado2 = comprueba_palabras(nombre_alumno="Román", palabras=sys.argv[1:])
print("="*100)
resultado3 = comprueba_solo_frutas(nombre_alumno="Román", palabras=sys.argv[1:])

resultado4 = dime_que_hacer(nombre_alumno="Román")
