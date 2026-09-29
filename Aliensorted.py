def isAlienSorted(palabras, orden):
    # crear mapa del diccionario alien

    mapa_dic = {c: i for i, c in enumerate(orden)}

    # revisar el orden de las palabras
    for i in range(
        len(palabras) - 1
    ):  # O(m) y TO(n) con n = len(palabras) y m = len(orden)
        palabra1 = palabras[i]
        palabra2 = palabras[i + 1]

        # comparar las palabras
        for j in range(min(len(palabra1), len(palabra2))):
            if palabra1[j] != palabra2[j]:
                if mapa_dic[palabra1[j]] > mapa_dic[palabra2[j]]:
                    return False
                break
        else:
            # Si todas las letras son iguales, verificar la longitud
            if len(palabra1) > len(palabra2):
                return False
    return True


# Ejemplo de uso
palabras = ["hello", "leetcode"]
orden = "hlabcdefgijkmnopqrstuvwxyz"

print(isAlienSorted(palabras, orden))
