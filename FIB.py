def fib(n, k):
    lst_fib = [0,1]
    for _ in range(n-1):
        lst_fib.append(lst_fib[-1] + k * lst_fib[-2])
    return lst_fib[-1]

fib(5, 3)
