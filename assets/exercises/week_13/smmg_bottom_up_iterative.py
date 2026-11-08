def weighted_max_stable_set(path_graph, weights):
    """
    Iterativer Brute-Force-Algorithmus zur Berechnung der stabilen Menge maximalen Gewichts eines Pfadgraphen.

    :param path_graph: Liste von Knoten des Pfadgraphen (als Indizes 0 bis n-1).
    :param weights: Liste der Gewichte der Knoten.
    :return: Maximalgewicht der stabilen Menge und die Menge selbst.
    """
    n = len(path_graph)
    if n == 0:
        print("Der Pfadgraph ist leer. Keine stabile Menge möglich.\n")
        return 0, []

    # Arrays zum Speichern der Ergebnisse
    dp = [0] * (n + 1)  # dp[i] speichert das maximale Gewicht bis zum Knoten i
    solution = [[] for _ in range(n + 1)]  # Lösungsmengen für jedes i

    print(f"Initialisierung: dp = {dp}, solution = {solution}\n")

    for i in range(n):
        print(f"Betrachte Knoten {i} mit Gewicht {weights[i]}.")

        # Fall 1: Ausschließen des aktuellen Knotens
        exclude_weight = dp[i]
        exclude_set = solution[i]
        print(f"  Option 1: Ausschließen von Knoten {i}, Gewicht = {exclude_weight}, Menge = {exclude_set}")

        # Fall 2: Einschließen des aktuellen Knotens
        include_weight = weights[i] + (dp[i - 1] if i > 0 else 0)
        include_set = ([i] + solution[i - 1]) if i > 0 else [i]
        print(f"  Option 2: Einschließen von Knoten {i}, Gewicht = {include_weight}, Menge = {include_set}")

        # Wähle die bessere Option
        if include_weight > exclude_weight:
            dp[i + 1] = include_weight
            solution[i + 1] = include_set
            print(f"  Wähle Option 2: dp[{i + 1}] = {dp[i + 1]}, Lösung = {solution[i + 1]}")
        else:
            dp[i + 1] = exclude_weight
            solution[i + 1] = exclude_set
            print(f"  Wähle Option 1: dp[{i + 1}] = {dp[i + 1]}, Lösung = {solution[i + 1]}")

    print(f"\nStabile Menge maximalen Gewichts: {solution[n]} mit Gewicht {dp[n]}\n")
    return dp[n], solution[n]


# Beispielaufruf
if __name__ == '__main__':
    path_graph = [0, 1, 2, 3]  # Knoten 0 bis 3
    weights = [1, 4, 5, 4]    # Gewichte der Knoten
    weighted_max_stable_set(path_graph, weights)
