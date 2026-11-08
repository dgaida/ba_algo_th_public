# Rekursive Brute-Force-Implementierung der Fibonacci-Zahlen
def fibonacci_recursive(n):
    """
    Berechnet die n-te Fibonacci-Zahl rekursiv (Brute-Force).

    :param n: Die Position der Fibonacci-Zahl.
    :return: Die n-te Fibonacci-Zahl.
    """
    print(f"Berechne fibonacci_recursive({n})")
    if n <= 1:
        print(f"  Basisfall erreicht: fibonacci_recursive({n}) = {n}")
        return n
    result = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    print(f"  fibonacci_recursive({n}) = {result}")
    return result


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
        print(f"Memo-Treffer: fibonacci_memoization({n}) = {memo[n]}")
        return memo[n]
    print(f"Berechne fibonacci_memoization({n})")
    if n <= 1:
        memo[n] = n
        print(f"  Basisfall erreicht: fibonacci_memoization({n}) = {n}")
    else:
        memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
        print(f"  fibonacci_memoization({n}) = {memo[n]}")
    return memo[n]


# Bottom-up-Ansatz mit Array
def fibonacci_bottom_up_array(n):
    """
    Berechnet die n-te Fibonacci-Zahl mit einem Bottom-up-Ansatz und einem Array.

    :param n: Die Position der Fibonacci-Zahl.
    :return: Die n-te Fibonacci-Zahl.
    """
    print(f"Berechne fibonacci_bottom_up_array({n})")
    if n <= 1:
        print(f"  Basisfall erreicht: fibonacci_bottom_up_array({n}) = {n}")
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    print(f"  Initialisiere Array: {fib}")
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
        print(f"  fib[{i}] = {fib[i]} (berechnet als fib[{i - 1}] + fib[{i - 2}])")
    print(f"  Ergebnis: fibonacci_bottom_up_array({n}) = {fib[n]}")
    return fib[n]


# Bottom-up-Ansatz ohne Array
def fibonacci_bottom_up_optimized(n):
    """
    Berechnet die n-te Fibonacci-Zahl mit einem Bottom-up-Ansatz ohne ein Array (nur zwei Variablen).

    :param n: Die Position der Fibonacci-Zahl.
    :return: Die n-te Fibonacci-Zahl.
    """
    print(f"Berechne fibonacci_bottom_up_optimized({n})")
    if n <= 1:
        print(f"  Basisfall erreicht: fibonacci_bottom_up_optimized({n}) = {n}")
        return n
    a, b = 0, 1
    print(f"  Initialisiere: a = {a}, b = {b}")
    for i in range(2, n + 1):
        a, b = b, a + b
        print(f"  Iteration {i}: a = {a}, b = {b}")
    print(f"  Ergebnis: fibonacci_bottom_up_optimized({n}) = {b}")
    return b


# Beispiele
if __name__ == '__main__':
    n = 9
    print("Rekursive Brute-Force:", fibonacci_recursive(n))
    print("Rekursiv mit Memoization:", fibonacci_memoization(n))
    print("Bottom-up mit Array:", fibonacci_bottom_up_array(n))
    print("Bottom-up ohne Array:", fibonacci_bottom_up_optimized(n))
