from random import randint
from timeit import repeat

# These imports are necessary even though it sees as not being used
from algorithms.ds.sorting.BubbleSort import bubble_sort
from algorithms.ds.sorting.InsertionSort import insertion_sort
from algorithms.ds.sorting.MergeSort import merge_sort
from algorithms.ds.sorting.QuickSort import quick_sort


def run_sorting_algorithm(algorithm, array_to_sort):
    setup_code = f"from __main__ import {algorithm}"

    stmt = f"{algorithm}({array_to_sort})"

    # number=10 -- each time 10 executions which repeats (repeat=3) 3 times and thus gives list of 3 values in seconds
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    # print(times)

    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


if __name__ == "__main__":
    desired_arr_length = 1000
    arr = [randint(0, 1000) for i in range(desired_arr_length)]

    run_sorting_algorithm(algorithm="bubble_sort", array_to_sort=arr)
    run_sorting_algorithm(algorithm="insertion_sort", array_to_sort=arr)
    run_sorting_algorithm(algorithm="merge_sort", array_to_sort=arr)
    run_sorting_algorithm(algorithm="quick_sort", array_to_sort=arr)
