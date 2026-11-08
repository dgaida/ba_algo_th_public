def weighted_max_stable_set(path_graph, weights):
    """
    Rekursiver Brute-Force-Algorithmus zur Berechnung der stabilen Menge maximalen Gewichts eines Pfadgraphen.

    :param path_graph: Liste von Knoten des Pfadgraphen (als Indizes 0 bis n-1).
    :param weights: Liste der Gewichte der Knoten.
    :return: Maximalgewicht der stabilen Menge und die Menge selbst.
    """
    def helper(index):
        if index < 0:
            print(f"Erreiche Anfang des Pfades. Kein Beitrag mehr.\n")
            return 0, []

        print(f"Betrachte Knoten {index} mit Gewicht {weights[index]}.")

        # Fall 1: Knoten wird ausgeschlossen
        print(f"  Option 1: Ausschließen von Knoten {index}.")
        exclude_weight, exclude_set = helper(index - 1)

        # Fall 2: Knoten wird eingeschlossen (überspringe den vorherigen Nachbarn)
        print(f"  Option 2: Einschließen von Knoten {index}.")
        include_weight, include_set = helper(index - 2)
        include_weight += weights[index]
        include_set = [index] + include_set

        # Vergleiche die beiden Optionen
        if include_weight > exclude_weight:
            print(f"  Wähle Option 2: Einschließen von Knoten {index} mit Gesamtgewicht {include_weight}.")
            return include_weight, include_set
        else:
            print(f"  Wähle Option 1: Ausschließen von Knoten {index} mit Gesamtgewicht {exclude_weight}.")
            return exclude_weight, exclude_set

    max_weight, stable_set = helper(len(path_graph) - 1)
    print(f"\nStabile Menge maximalen Gewichts: {stable_set} mit Gewicht {max_weight}\n")
    return max_weight, stable_set


# Beispielaufruf
if __name__ == '__main__':
    path_graph = [0, 1, 2, 3]  # Knoten 0 bis 3
    weights = [1, 4, 5, 4]    # Gewichte der Knoten
    weighted_max_stable_set(path_graph, weights)
