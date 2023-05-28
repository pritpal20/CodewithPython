from common.helper_functions import create_array
import pytest
import sys

print(create_array(10))

@pytest.mark.parametrize("n",
        [
            pytest.param(10),
            pytest.param(20),
            pytest.param(30),
            pytest.param(100),
        ]
)
def test_create_array(n):

    arr = create_array(n)

    val = False
    for i in range(-n,n):

        if i in arr:
            val = True
        else:
            val = False
            return
        
    assert val == True

@pytest.mark.parametrize("n",
        [
            pytest.param(-10),
            pytest.param(-1),
            
        ]
)
def test_create_array_negative_args(n):

    with pytest.raises(ValueError):
        arr = create_array(n)
    

if __name__ == "__main__":

    ret = pytest.main(["-vs",__file__])
    sys.exit(ret)        

