def solucion():
    def rotar(pieza):
        rotada = ''
        if 'N' in pieza:
            rotada += 'E'
        if 'E' in pieza:
            rotada += 'S'
        if 'S' in pieza:
            rotada += 'W'
        if 'W' in pieza:
            rotada += 'N'
        return rotada

    def es_valido(cuadricula):
        R = len(cuadricula)
        C = len(cuadricula[0])
        for r in range(R):
            for c in range(C):
                pieza = cuadricula[r][c]
                # Verificar Norte
                if 'N' in pieza:
                    if r == 0 or 'S' not in cuadricula[r-1][c]:
                        return False
                # Verificar Este
                if 'E' in pieza:
                    if c == C-1 or 'W' not in cuadricula[r][c+1]:
                        return False
                # Verificar Sur
                if 'S' in pieza:
                    if r == R-1 or 'N' not in cuadricula[r+1][c]:
                        return False
                # Verificar Oeste
                if 'W' in pieza:
                    if c == 0 or 'E' not in cuadricula[r][c-1]:
                        return False
        return True

    def backtracking(cuadricula, r, c):
        if r == R:
            return es_valido(cuadricula)

        siguiente_r = r
        siguiente_c = c + 1
        if siguiente_c == C:
            siguiente_r += 1
            siguiente_c = 0

        pieza = cuadricula[r][c]
        for _ in range(4):
            if backtracking(cuadricula, siguiente_r, siguiente_c):
                return True
            cuadricula[r][c] = rotar(cuadricula[r][c])
        cuadricula[r][c] = pieza  # Restaurar pieza original
        return False

    while True:
        R, C = map(int, input().split())
        if R == 0 and C == 0:
            break

        cuadricula = []
        for _ in range(R):
            fila = input().split()
            cuadricula.append(fila)

        if backtracking(cuadricula, 0, 0):
            print("SOLUCIONABLE")
        else:
            print("NOSOLUCIONABLE")

solucion()
