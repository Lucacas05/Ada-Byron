def solucion():
    while True:
        n = int(input())
        if n == 0:
            break

        donaciones = list(map(int, input().split()))

        conteo = {}
        for donacion in donaciones:
            conteo[donacion] = conteo.get(donacion, 0) + 1

        repetido = None
        conteo_max = 0

        for donacion, conteo_val in conteo.items():
            if repetido is None or conteo_val > conteo_max:
                repetido = donacion
                conteo_max = conteo_val
            elif conteo_val == conteo_max and donacion < repetido:
                repetido = donacion

        print(repetido)

solucion()
