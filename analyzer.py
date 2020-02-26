import time
from demos import quicksort, mergesort, bubblesort
from random import randint

'''Generate lists of random integers'''
def create_random_list(size, max_val):
    return [randint(1, max_val) for num in range(size)]

'''Calculate and display the time it took to run function'''
# time (seconds) returns an instance of the current
# time based on the system
def analyze_func(func_name, arr):
    tic = time.time()
    func_name(arr)
    toc = time.time()
    seconds = toc - tic
    # use dunder name so actual function name prints
    # otherwise shows memory location
    print(f"{func_name.__name__.capitalize()}\t-> Elapsed time:  {seconds:.5f}")

'''List size and range of integer values will be
specified by user at run-time'''
size = int(input("What size list do you want to create? "))
max = int(input("What is the max value of the range? "))
run_times = int(input("How many time do you want to run? "))

for num in range(run_times):
    print(f"Run: {num+1}")
    l = create_random_list(size, max)
    analyze_func(bubblesort, l.copy())
    analyze_func(quicksort, l)
    analyze_func(mergesort, l)
    analyze_func(sorted, l)
    print("-" * 40)

# used copy() method since bubblesort does not return anything
# to prevent the list from being sorted
# if the other sort algorithms were run after,
# it would return the runtime of the the sorted list


