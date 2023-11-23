liste_1 = [732, 291, 72, 7, 92]
liste_2 = [910, 3, 270, 19, 32]

def bubble_sort(arr):
    n = 0
    for _ in arr:
        n += 1

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)

bubble_sort(liste_1)
bubble_sort(liste_2)