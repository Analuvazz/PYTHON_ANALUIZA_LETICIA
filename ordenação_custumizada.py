def custom_sort_key(item):
    return len(item)

atributo = ["Deliniador","Rimel","Base","Blush"]
atributo_ordenado = sorted(atributo, key=custom_sort_key)
print(atributo_ordenado)
