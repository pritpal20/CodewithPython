
from common.helper_functions import create_array_unsigned

def bubble_sort(arr : list ):

    n = len(arr)
    for i in range(n-1) :
        for j in range(i+1,n):
            if( arr[i] > arr[j]):
                arr[i],arr[j] = arr[j],arr[i]
    return arr

def insertion_sort(arr : list):
    n = len(arr)

    for i in range(n - 1):
        j = i + 1 
        while arr[j-1] > arr[j] and j > 0 :

            arr[j-1],arr[j] = arr[j],arr[j-1]
            j = j - 1

    