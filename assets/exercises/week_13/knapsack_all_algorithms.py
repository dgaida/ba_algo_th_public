# Rekursive Brute-Force-Implementierung des 0-1-Rucksackproblems
def knapsack_recursive(weights, values, capacity, n):
    """
    Rekursive Brute-Force-Lösung des 0-1-Rucksackproblems.

    :param weights: Liste der Gewichte der Gegenstände.
    :param values: Liste der Werte der Gegenstände.
    :param capacity: Maximale Kapazität des Rucksacks.
    :param n: Anzahl der verfügbaren Gegenstände.
    :return: Maximaler Wert, der im Rucksack erreicht werden kann.
    """
    print(f"Berechne knapsack_recursive(n={n}, capacity={capacity})")

    # Basisfall: Keine Gegenstände oder keine Kapazität mehr
    if n == 0 or capacity == 0:
        print(f"  Basisfall erreicht: n={n}, capacity={capacity} -> Wert = 0")
        return 0

    # Fall: Gewicht des aktuellen Gegenstands ist größer als die verbleibende Kapazität
    if weights[n - 1] > capacity:
        print(f"  Gegenstand {n} passt nicht in den Rucksack (Gewicht: {weights[n - 1]} > Kapazität: {capacity})")
        return knapsack_recursive(weights, values, capacity, n - 1)

    # Zwei Fälle: Gegenstand n wird entweder gewählt oder nicht gewählt
    without_item = knapsack_recursive(weights, values, capacity, n - 1)
    with_item = values[n - 1] + knapsack_recursive(weights, values, capacity - weights[n - 1], n - 1)

    result = max(without_item, with_item)
    print(f"  Maximaler Wert mit n={n}, capacity={capacity}: max({without_item}, {with_item}) = {result}")
    return result


# Rekursive Implementierung mit Memoization
def knapsack_memoization(weights, values, capacity, n, memo=None):
    """
    Rekursive Lösung des 0-1-Rucksackproblems mit Memoization.

    :param weights: Liste der Gewichte der Gegenstände.
    :param values: Liste der Werte der Gegenstände.
    :param capacity: Maximale Kapazität des Rucksacks.
    :param n: Anzahl der verfügbaren Gegenstände.
    :param memo: Memo-Dictionary zur Speicherung bereits berechneter Werte.
    :return: Maximaler Wert, der im Rucksack erreicht werden kann.
    """
    if memo is None:
        memo = {}

    print(f"Berechne knapsack_memoization(n={n}, capacity={capacity})")

    # Basisfall: Keine Gegenstände oder keine Kapazität mehr
    if n == 0 or capacity == 0:
        print(f"  Basisfall erreicht: n={n}, capacity={capacity} -> Wert = 0")
        return 0

    # Prüfen, ob das Ergebnis bereits berechnet wurde
    if (n, capacity) in memo:
        print(f"  Memo-Treffer: memo[({n}, {capacity})] = {memo[(n, capacity)]}")
        return memo[(n, capacity)]

    # Fall: Gewicht des aktuellen Gegenstands ist größer als die verbleibende Kapazität
    if weights[n - 1] > capacity:
        print(f"  Gegenstand {n} passt nicht in den Rucksack (Gewicht: {weights[n - 1]} > Kapazität: {capacity})")
        memo[(n, capacity)] = knapsack_memoization(weights, values, capacity, n - 1, memo)
    else:
        without_item = knapsack_memoization(weights, values, capacity, n - 1, memo)
        with_item = values[n - 1] + knapsack_memoization(weights, values, capacity - weights[n - 1], n - 1, memo)
        memo[(n, capacity)] = max(without_item, with_item)

    print(f"  Maximaler Wert mit n={n}, capacity={capacity}: {memo[(n, capacity)]}")
    return memo[(n, capacity)]


# Bottom-up-Ansatz des 0-1-Rucksackproblems
def knapsack_bottom_up(weights, values, capacity):
    """
    Bottom-up-Lösung des 0-1-Rucksackproblems.

    :param weights: Liste der Gewichte der Gegenstände.
    :param values: Liste der Werte der Gegenstände.
    :param capacity: Maximale Kapazität des Rucksacks.
    :return: Maximaler Wert, der im Rucksack erreicht werden kann.
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    print(f"Initialisiere DP-Tabelle mit Größe ({n+1}, {capacity+1})")

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
                print(f"  dp[{i}][{w}] = {dp[i][w]} (Gegenstand {i} passt nicht)")
            else:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
                print(f"  dp[{i}][{w}] = max(dp[{i - 1}][{w}], values[{i - 1}] + dp[{i - 1}][{w - weights[i - 1]}]) = {dp[i][w]}")

    print(f"Maximaler Wert: {dp[n][capacity]}")
    return dp[n][capacity]


# Beispielaufrufe
if __name__ == '__main__':
    weights = [1, 2, 3, 4]
    values = [10, 20, 30, 40]
    capacity = 5

    print("Rekursive Brute-Force:")
    print(knapsack_recursive(weights, values, capacity, len(weights)))

    print("\nRekursiv mit Memoization:")
    print(knapsack_memoization(weights, values, capacity, len(weights)))

    print("\nBottom-up-Ansatz:")
    print(knapsack_bottom_up(weights, values, capacity))
