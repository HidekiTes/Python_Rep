lista = [6,8,5,4,1,41,85,3,410,63,4106,40,14,16,38,56,44,165,84,632]

def bubble_sort(arr):

    n = len(arr)

    # Para cada elemento i do array
    for i in range(n):
        # Para cada elemento j do array
        for j in range(0, n-i-1):
            # Se elemento i for maior que elemento j 
            if arr[j] > arr[j+1]:
                #Troque os elementos i e j
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print (bubble_sort(lista))

lista2 = [60,80,50,4,1,41,85,3,410,63,4106,40,14,16,38,56,44,165,84,632]
print (bubble_sort(lista2))