def find_next_min(arr, i):
    # Finde den Index des kleinsten Elements im Rest der Liste
    min_index = i
    for j in range(i + 1, len(arr)):
        print(f"  Vergleiche arr[{min_index}] ({arr[min_index]}) mit arr[{j}] ({arr[j]})")
        if arr[j] < arr[min_index]:
            print(f"  -> arr[{j}] ({arr[j]}) ist kleiner. Aktualisiere min_index auf {j}")
            min_index = j

    return min_index


def swap(arr, min_index, i):
    # Tausche das kleinste gefundene Element mit dem ersten Element des unsortierten Bereichs
    if min_index != i:
        print(f"Tausche arr[{i}] ({arr[i]}) mit arr[{min_index}] ({arr[min_index]})")
        arr[i], arr[min_index] = arr[min_index], arr[i]
    else:
        print(f"Kein Tausch nötig, da arr[{i}] bereits das kleinste Element ist")


def selection_sort(arr):
    print(f"Initiale Liste: {arr}\n")

    # Gehe jedes Element der Liste durch
    for i in range(len(arr)):
        print(f"Iteration {i + 1}:\nAktuelle Liste: {arr}")

        min_index = find_next_min(arr, i)

        swap(arr, min_index, i)

        print(f"Ergebnis nach Iteration {i + 1}: {arr}\n")

    print(f"Sortierte Liste: {arr}")


# Beispielaufruf
if __name__ == '__main__':
    liste = [64, 25, 12, 22, 11]
    selection_sort(liste)
