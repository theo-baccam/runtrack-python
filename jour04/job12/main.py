liste_1 = [732, 291, 72, 7, 92]
liste_2 = [910, 3, 270, 19, 32]

# Algorithme bubble sort
# L'algortithme parcourt plusieurs fois la liste, et compare deux éléments adjacents
# si un élément est plus grand que son prochain, il les changent de place
# Ca se répête jusqu'à que la liste soit complétement en ordre croissant.

def bubble_sort(arr):
    n = 0           # Pour trouver la longuer de la liste sans len
    for _ in arr:
        n += 1

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)

bubble_sort(liste_1)
bubble_sort(liste_2)