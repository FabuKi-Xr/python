def mergeSort(array,count=0):
    
    if len(array) > 1:

        r = len(array)//2
        L = array[:r]
        M = array[r:]

        count = mergeSort(L,count)
        count = mergeSort(M,count)

        i = j = k = 0

        while i < len(L) and j < len(M):
            count+=1
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
    return count
print(' *** Merge sort ***')
arr = list(map(int,input('Enter some numbers : ').split()))
count = mergeSort(arr)
print('\nSorted -> ',end="")
print(*arr,sep=" ")
print("Data comparison =  "+str(count))
