import pytest
import sys

from common.helper_functions import create_array
from Sorting.sorting import quick_sort

@pytest.mark.parametrize(
    "n",
    [
        (10),
        (50),
        (100),
        (1000),
    ],
)
def test_quick_sort(n):
    arr1 = [i for i in range(-n, n)]

    arr2 = create_array(n)
    N = len(arr2)
    quick_sort(arr2,0,N - 1)

    assert arr1 == arr2



if __name__ == "__main__":
    ret = pytest.main(
        [
            "-vs",
            __file__,
        ]
    )
    sys.exit(ret)
