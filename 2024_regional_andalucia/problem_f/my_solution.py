def es_seguro(numero):
    if numero <= 0: # no se puede usar números menores o iguales a 0
        return False
        
    texto_numero = str(numero)
    cantidad_digitos = len(texto_numero)
    
    suma_potencias = 0
    
    for digito_char in texto_numero:
        digito_int = int(digito_char)
        try:
            # Usar exponenciación entera
            potencia = pow(digito_int, cantidad_digitos)
            suma_potencias += potencia
        except OverflowError:
            # Manejar casos donde el resultado es demasiado grande (aunque improbable con n < 100000)
            return False
        # Opcional: Comprobar si la suma ya excede el número para optimizar
        # if suma_potencias > numero:
        #     return False # No puede ser igual si ya se pasó
            
    return suma_potencias == numero

def resolver():
    while True:
        try:
            # Leer el número n
            n_texto = input()
            # Si la línea está vacía, intentar leer de nuevo (puede pasar con algunas redirecciones)
            if not n_texto: 
                continue
            n = int(n_texto)
            
            # La señal de terminación es 0
            if n == 0:
                break 
                
            # Comprobar si es seguro y mostrar el resultado
            if es_seguro(n):
                print("SEGURO")
            else:
                print("INSEGURO")
                
        except EOFError:
            # Se alcanzó el final de la entrada
            break
        except ValueError:
            # Manejar formato de número inválido
            # print("Entrada inválida.") 
            break # Terminar si la entrada no es un número válido

# Ejecutar la función principal cuando se corre el script
if __name__ == "__main__":
    resolver()
