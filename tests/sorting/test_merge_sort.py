import random

from sorting.merge_sort import mergesort

def test_mergesort():
    assert mergesort([]) == []
    assert mergesort([0]) == [0]

    sample_list = [5, 3, 6, 8, 3, 4]
    assert mergesort(sample_list) == [3, 3, 4, 5, 6, 8]

    for i in range(100):
        random.seed(0)
        list_size = random.randint(0, 1000)
        sample_list = [random.randint(-100, 100) for i in range(list_size)]
        assert mergesort(sample_list) == sorted(sample_list)