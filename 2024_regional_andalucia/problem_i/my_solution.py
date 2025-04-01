def solucion():
    while True:
        n = int(input())
        if n == 0:
            break
        ventas = list(map(int, input().split()))
        are = []
        stack = []
        for i in range(n):
            while stack and ventas[stack[-1]] <= ventas[i]:
                stack.pop()
            if not stack:
                are.append(i + 1)
            else:
                are.append(i - stack[-1])
            stack.append(i)
        print(' '.join(map(str, are)))

solucion()