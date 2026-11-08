def bucket_sort_integer(arr, K):
    """
    Sortiert eine Liste von Integern, die zwischen 1 und K liegen.
    """
    print(f"Initiale Liste: {arr}\n")
    if len(arr) == 0:
        return arr

    # Erstelle K Buckets (eine Liste von Listen)
    buckets = [[] for _ in range(K)]

    # Verteile die Elemente auf die Buckets
    for num in arr:
        print(f"  Füge {num} in Bucket {num - 1} ein")
        buckets[num - 1].append(num)

    print(f"Buckets nach dem Einsortieren: {buckets}\n")

    # Führe die Buckets zusammen
    sorted_arr = []
    for i, bucket in enumerate(buckets):
        print(f"  Füge Bucket {i} hinzu: {bucket}")
        sorted_arr.extend(bucket)

    print(f"Sortierte Liste: {sorted_arr}\n")
    return sorted_arr


def bucket_sort_float(arr):
    """
    Sortiert eine Liste von Float-Zahlen zwischen 0 und 1.
    """
    print(f"Initiale Liste: {arr}\n")
    if len(arr) == 0:
        return arr

    # Anzahl der Buckets bestimmen
    bucket_count = len(arr)
    print(f"Anzahl Buckets: {bucket_count}")

    # Erstelle Buckets
    buckets = [[] for _ in range(bucket_count)]

    # Verteile die Elemente auf die Buckets
    for num in arr:
        index = int(num * bucket_count)  # Skalierung der Float-Werte in Buckets
        print(f"  Füge {num} in Bucket {index} ein")
        buckets[index].append(num)

    print(f"Buckets nach dem Einsortieren: {buckets}\n")

    # Sortiere jeden Bucket und führe sie zusammen
    sorted_arr = []
    for i, bucket in enumerate(buckets):
        print(f"  Sortiere Bucket {i}: {bucket}")
        sorted_bucket = sorted(bucket)
        print(f"    Sortierter Bucket {i}: {sorted_bucket}")
        sorted_arr.extend(sorted_bucket)

    print(f"Sortierte Liste: {sorted_arr}\n")
    return sorted_arr


# Beispielaufruf für Integer
if __name__ == '__main__':
    print("Bucket Sort für Integer:")
    integer_list = [4, 2, 2, 8, 3, 3, 1]
    K = 8
    bucket_sort_integer(integer_list, K)

    # Beispielaufruf für Float
    print("Bucket Sort für Float:")
    float_list = [0.64, 0.25, 0.12, 0.22, 0.11]
    bucket_sort_float(float_list)
