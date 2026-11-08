def find_spot(arr, current_index):
    """
    Findet die richtige Position für das aktuelle Element (arr[current_index]) im sortierten Bereich.
    """
    value = arr[current_index]
    print(f"  Finde die richtige Position für arr[{current_index}] ({value})")

    # Gehe zurück im sortierten Bereich, um die richtige Position zu finden
    while current_index > 0 and arr[current_index - 1] > value:
        print(f"    arr[{current_index - 1}] ({arr[current_index - 1]}) > {value}, verschiebe nach links")
        current_index -= 1

    print(f"  Richtige Position gefunden: {current_index}\n")
    return current_index


def shift(arr, start, end):
    """
    Verschiebt Elemente von Index `start` bis `end` nach rechts, um Platz zu machen.
    """
    print(f"  Schiebe Elemente von Index {start} bis {end - 1} nach rechts")
    for i in range(end, start, -1):
        arr[i] = arr[i - 1]
        print(f"    arr[{i}] wird zu arr[{i - 1}] ({arr[i]})")


def insertion_sort(arr):
    print(f"Initiale Liste: {arr}\n")

    # Gehe jedes Element ab dem zweiten durch
    for i in range(1, len(arr)):
        print(f"Iteration {i}:\nAktuelle Liste: {arr}")

        # Finde die richtige Position im sortierten Bereich
        spot = find_spot(arr, i)

        # Speichere das aktuelle Element und verschiebe Elemente
        if spot != i:
            value_to_insert = arr[i]
            shift(arr, spot, i)

            # Setze das Element an die richtige Position
            arr[spot] = value_to_insert
            print(f"  Setze {value_to_insert} an Position {spot}")
        else:
            print(f"  Kein Verschieben notwendig, {arr[i]} ist bereits an der richtigen Stelle")

        print(f"Ergebnis nach Iteration {i}: {arr}\n")

    print(f"Sortierte Liste: {arr}")


# Beispielaufruf
if __name__ == '__main__':
    liste = [64, 25, 12, 22, 11]
    insertion_sort(liste)
