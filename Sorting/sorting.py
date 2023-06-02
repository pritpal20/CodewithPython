from common.helper_functions import create_array_unsigned


def bubble_sort(arr: list):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def insertion_sort(arr: list):
    n = len(arr)

    for i in range(n - 1):
        j = i + 1
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j = j - 1


def partition(arr, start, end):
    """
    partition the array into two
    """
    p = end
    for i in range(start, p):
        while arr[i] > arr[p] and i < p:
            arr[i], arr[p] = arr[p], arr[i]
            p = p - 1
            arr[i], arr[p] = arr[p], arr[i]

    return p


def quick_sort(arr: list, start: int, end: int):
    """ 
    quick sort 
    """
    if start >= end:
        return

    p = partition(arr, start, end)
    quick_sort(arr, start, p - 1)
    quick_sort(arr, p + 1, end)
