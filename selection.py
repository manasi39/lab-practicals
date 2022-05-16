#Selection
def selectionSort(array):
    n=len(array)
    for i in range(n):
        min=i

        for j in range(i+1,n):
            if(array[j]<array[min]):
                min=j

        temp=array[i]
        array[i]=array[min]
        array[min]=temp

    return array

array=[13,7,2,9,18,6,15]
print(selectionSort(array))



