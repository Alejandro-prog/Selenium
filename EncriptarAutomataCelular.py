import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

# Metodo para encriptar 
def encriptar():
  # Obtenemos mensaje a cifrar desde el usuario
  # llamamos a upper para obtener sólo mayúsculas
  y = input("Mensaje: ").upper()

  # Pedimos al usuario la cantidad de desplazamiento
  x = int(input("Desplazamiento: "))
  
  # Abecedario a utilizar en el cifrado
  abc = "#ABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234"

  # Variable para guardar mensaje cifrado
  cifrado = ""

  # Iteramos por cada letra del mensaje
  for elemento in y:
      # Si la letra está en el abecedario se reemplaza
      if elemento in abc:
          pos_letra = abc.index(elemento)
          # Sumamos para movernos a la derecha del abc teniendo en cuenta el modulo
          nueva_pos = (pos_letra + x) % len(abc)
          cifrado+= abc[nueva_pos]
      else:
          # Si no está en el abecedario sólo añadelo
          cifrado += elemento

  print("Mensaje cifrado: ", cifrado)
  
