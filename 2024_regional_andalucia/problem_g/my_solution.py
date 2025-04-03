import sys
from collections import deque

def is_bipartite(n, adj):
    color = [0] * (n + 1)  # 0: sin color, 1: color 1, 2: color 2
    for i in range(1, n + 1):
        if color[i] == 0:  # Si el nodo i aún no está coloreado (parte de un nuevo componente)
            q = deque()
            q.append(i)
            color[i] = 1  # Empezar a colorear con el color 1
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == 0:  # Si el vecino no está coloreado
                        color[v] = 3 - color[u]  # Asignar el color opuesto
                        q.append(v)
                    elif color[v] == color[u]:  # Si el vecino tiene el mismo color
                        return False  # Conflicto: el grafo no es bipartito
    return True # No se encontraron conflictos, el grafo es bipartito

def solve():
    T = int(sys.stdin.readline()) # Leer número de casos de prueba
    for _ in range(T):
        n, m = map(int, sys.stdin.readline().split()) # Leer n (amigos) y m (rivalidades)
        adj = [[] for _ in range(n + 1)] # Inicializar lista de adyacencia
        for __ in range(m):
            u, v = map(int, sys.stdin.readline().split()) # Leer una rivalidad
            # Añadir aristas para la rivalidad (grafo no dirigido)
            adj[u].append(v)
            adj[v].append(u)

        # Comprobar si el grafo es bipartito e imprimir el mensaje correspondiente
        if is_bipartite(n, adj):
            print("Que comience la batalla")
        else:
            print("Mejor nos vamos de cena o algo")

if __name__ == "__main__":
    solve()