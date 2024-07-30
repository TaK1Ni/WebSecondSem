cube = lambda x: x**3

def fibonacci(n):
    if n == 1:
        return 0
    arr_fib = [0, 1]
    while len(arr_fib) < n:
        arr_fib.append(arr_fib[-1] + arr_fib[-2])
    return arr_fib


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
