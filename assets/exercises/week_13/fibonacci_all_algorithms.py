# Rekursive Brute-Force-Implementierung der Fibonacci-Zahlen
def fibonacci_recursive(n):
    """
    Berechnet die n-te Fibonacci-Zahl rekursiv (Brute-Force).

    :param n: Die Position der Fibonacci-Zahl.
    :return: Die n-te Fibonacci-Zahl.
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Rekursive Implementierung mit Memoization
def fibonacci_memoization(n, memo=None):
    """
    Berechnet die n-te Fibonacci-Zahl rekursiv mit Memoization.

    :param n: Die Position der Fibonacci-Zahl.
    :param memo: Dictionary zur Speicherung bereits berechneter Fibonacci-Zahlen.
    :return: Die n-te Fibonacci-Zahl.
    """
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]


# Bottom-up-Ansatz mit Array
def fibonacci_bottom_up_array(n):
    """
    Berechnet die n-te Fibonacci-Zahl mit einem Bottom-up-Ansatz und einem Array.

    :param n: Die Position der Fibonacci-Zahl.
    :return: Die n-te Fibonacci-Zahl.
    """
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]


# Bottom-up-Ansatz ohne Array
def fibonacci_bottom_up_optimized(n):
    """
    Berechnet die n-te Fibonacci-Zahl mit einem Bottom-up-Ansatz ohne ein Array (nur zwei Variablen).

    :param n: Die Position der Fibonacci-Zahl.
    :return: Die n-te Fibonacci-Zahl.
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# Beispiele
if __name__ == '__main__':
    n = 9
    print("Rekursive Brute-Force:", fibonacci_recursive(n))
    print("Rekursiv mit Memoization:", fibonacci_memoization(n))
    print("Bottom-up mit Array:", fibonacci_bottom_up_array(n))
    print("Bottom-up ohne Array:", fibonacci_bottom_up_optimized(n))
