def merge_lists(nums1, n, nums2, m):
    p1 = n - 1
    p2 = m - 1
    p = len(nums1) - 1

    while 0 <= p1 and 0 <= p2:  # aun hay elementos en la lista
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1  # mover el puntero de la primera lista
        p -= 1  # mover el puntero de la lista combinada
    # T = O( n + m ) = O( n )
    # S = O( 1 )

    if n != m:
        nums1[: p2 + 1] = nums2[: p2 + 1]
        # Si la primera lista es más corta que la segunda, copiamos los elementos restantes de la segunda lista a la primera lista.

    return nums1


# Ejemplo de uso
nums1 = [1, 2, 3, 0, 0, 0]
n = 3

nums2 = [2, 5, 6]
m = 3

print(merge_lists(nums1, n, nums2, m))  # Salida: [1, 2, 2, 3, 5, 6]
