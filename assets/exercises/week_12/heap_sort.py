def heapify(arr, n, i):
    """
    Stellt sicher, dass der Teilbaum mit Wurzel bei Index i ein Max-Heap ist.
    """
    largest = i  # Wurzel
    left = 2 * i + 1  # Linkes Kind
    right = 2 * i + 2  # Rechtes Kind

    print(f"  Heapify auf Index {i}, linkes Kind: {left}, rechtes Kind: {right}")

    # Prüfe, ob das linke Kind größer ist als die Wurzel
    if left < n and arr[left] > arr[largest]:
        print(f"    arr[{left}] ({arr[left]}) ist größer als arr[{largest}] ({arr[largest]})")
        largest = left

    # Prüfe, ob das rechte Kind größer ist als der größte bisher
    if right < n and arr[right] > arr[largest]:
        print(f"    arr[{right}] ({arr[right]}) ist größer als arr[{largest}] ({arr[largest]})")
        largest = right

    # Tausche die Wurzel mit dem größten Kind, falls nötig
    if largest != i:
        print(f"    Tausche arr[{i}] ({arr[i]}) mit arr[{largest}] ({arr[largest]})")
        arr[i], arr[largest] = arr[largest], arr[i]

        # Rekursiv heapify für das betroffene Kind
        heapify(arr, n, largest)


def heapsort(arr):
    print(f"Initiale Liste: {arr}\n")

    n = len(arr)

    # Baue einen Max-Heap
    print("Baue Max-Heap:")
    for i in range(n // 2 - 1, -1, -1):
        print(f"Heapify für Index {i}:")
        heapify(arr, n, i)
        print(f"  Nach Heapify: {arr}\n")

    # Extrahiere Elemente aus dem Heap
    print("Heap sortieren:")
    for i in range(n - 1, 0, -1):
        print(f"Tausche arr[0] ({arr[0]}) mit arr[{i}] ({arr[i]})")
        arr[i], arr[0] = arr[0], arr[i]  # Tausche
        print(f"  Nach Tausch: {arr}")

        print(f"  Rufe Heapify für den verkleinerten Heap auf (Größe {i}):")
        heapify(arr, i, 0)
        print(f"  Nach Heapify: {arr}\n")

    print(f"Sortierte Liste: {arr}")


# Beispielaufruf
if __name__ == '__main__':
    liste = [64, 25, 12, 22, 11]
    heapsort(liste)
