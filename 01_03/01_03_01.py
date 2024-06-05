# Rekursiver Ansatz als Muster, welche Zahlen ermittelt werden sollen
def fibonacciZahlen(n):
    if n > 1:
        return fibonacciZahlen(n-1) + fibonacciZahlen(n-2)
    return n

fibonacci = []
for i in range(10):
    if i<=1:
        fibonacci.append(i)
    else:
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])

for num in fibonacci:
    print(num)

