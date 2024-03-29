# Fibonacci numbers module

def fib(n):
    """Write fibonacci series up to n"""

    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    """Return fibonacci series up to n"""

    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
    print(fib2(int(sys.argv[1])))