from collections import Counter

def solucion():
    letras = input() 
    n = int(input())
    palabras = [input() for _ in range(n)] # es como un bucle while para pedir el num de palabras correctas

    conteo_letras = Counter(letras) # creamos el diccionario para quitar las variables repetidas
    palabras_posibles = []

    for palabra in palabras:
        contador_palabra = Counter(palabra) # separamos los caracteres para saber si pueden formar palabra
        forma = True
        for char, conteo in contador_palabra.items(): # seleccionamos cada valor del diccionario
            if conteo_letras[char] < conteo:
                forma = False
                break
        if forma:
            palabras_posibles.append(palabra)

    if not palabras_posibles:
        print("No es posible")
    else:
        palabra_larga = max(palabras_posibles, key=len) # encontramos el maximo teniendo en cuenta la longitud por eso el key
        candidatas = [palabra for palabra in palabras_posibles if len(palabra) == len(palabra_larga)] # si tenemos la misma longitud la añadimos en una nueva lista de candidatas
        print(min(candidatas)) # seleccionamos la primera en orden lexigrafico, por eso usamos min

solucion()
