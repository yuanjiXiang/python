# fibonacci数列

nitems = int(input('前多少位：'))

def recur_fibo(n):
    """递归求fibonacci数"""
    if n <= 1:
        return n
    else:
        return(recur_fibo(n - 1) + recur_fibo(n - 2))
    
fibonacci = []

for i in range(0, nitems + 1):
    fibonacci.append(recur_fibo(i))

print(fibonacci)

