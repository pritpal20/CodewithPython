import pytest
import sys

from common.helper_functions import create_array
from Sorting.sorting import bubble_sort, insertion_sort


@pytest.mark.parametrize( "n",
    [
        (10),
        (20),
        (30),
        (100),
        (1000),
    ]
)
def test_bubble_sort(n):

    arr1 = [ i for i  in range(-n,n)]

    arr2 = create_array(n)
    bubble_sort(arr2)

    assert arr1 == arr2


@pytest.mark.parametrize( "n",
    [
        (10),
        (20),
        (30),
        (100),
        (1000),
    ]
)
def test_insertion_sort(n):

    arr1 = [ i for i  in range(-n,n)]

    arr2 = create_array(n)
    insertion_sort(arr2)

    assert arr1 == arr2

if __name__ == "__main__":
    
    ret = pytest.main(["-vs",__file__,])
    sys.exit(ret)