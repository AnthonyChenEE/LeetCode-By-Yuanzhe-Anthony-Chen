# F(0) = 0, F(1) = 1

def fib(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fib(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq

n = int(input())
print(fib(n))
