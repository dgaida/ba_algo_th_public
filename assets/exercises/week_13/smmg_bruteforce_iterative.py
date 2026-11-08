import itertools

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

    max_weight = 0
    best_set = []

    # Generiere alle möglichen Teilmengen des Pfadgraphen
    for subset in itertools.product([0, 1], repeat=n):
        current_set = [i for i in range(n) if subset[i] == 1]
        print(f"Prüfe Teilmenge: {current_set}")

        # Überprüfe, ob die Teilmenge stabil ist
        is_stable = True
        for i in range(len(current_set) - 1):
            if current_set[i] + 1 == current_set[i + 1]:
                is_stable = False
                print(f"  Nicht stabil: {current_set[i]} und {current_set[i + 1]} sind benachbart.")
                break

        if is_stable:
            # Berechne das Gewicht der stabilen Menge
            weight = sum(weights[i] for i in current_set)
            print(f"  Stabil mit Gewicht {weight}.")

            if weight > max_weight:
                max_weight = weight
                best_set = current_set
                print(f"  Neue beste Menge: {best_set} mit Gewicht {max_weight}")
        else:
            print(f"  Nicht stabil, übersprungen.\n")

    print(f"\nStabile Menge maximalen Gewichts: {best_set} mit Gewicht {max_weight}\n")
    return max_weight, best_set


# Beispielaufruf
if __name__ == '__main__':
    path_graph = [0, 1, 2, 3]  # Knoten 0 bis 3
    weights = [1, 4, 5, 4]    # Gewichte der Knoten
    weighted_max_stable_set(path_graph, weights)
