def merge(arr, left_half, right_half):
    # Mergen der beiden Hälften
    i = j = k = 0

    print(f"Mergen: {left_half} und {right_half}")
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            print(f"  Wähle {left_half[i]} von links")
            i += 1
        else:
            arr[k] = right_half[j]
            print(f"  Wähle {right_half[j]} von rechts")
            j += 1
        k += 1

    # Reste der linken Hälfte hinzufügen
    while i < len(left_half):
        arr[k] = left_half[i]
        print(f"  Füge restliches {left_half[i]} von links hinzu")
        i += 1
        k += 1

    # Reste der rechten Hälfte hinzufügen
    while j < len(right_half):
        arr[k] = right_half[j]
        print(f"  Füge restliches {right_half[j]} von rechts hinzu")
        j += 1
        k += 1

    print(f"Gemergt zu: {arr}\n")


def merge_sort(arr):
    print(f"Sortiere: {arr}")

    if len(arr) > 1:
        # Liste in zwei Hälften teilen
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        print(f"Teile in: {left_half} und {right_half}\n")

        # Rekursives Sortieren der Hälften
        merge_sort(left_half)
        merge_sort(right_half)

        merge(arr, left_half, right_half)


# Beispielaufruf
if __name__ == '__main__':
    liste = [64, 25, 12, 22, 11]
    merge_sort(liste)
    print(f"Sortierte Liste: {liste}")
