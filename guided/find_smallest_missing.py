def find_smallest_missing(arr):
    # edge case: where 0 is missing, make sure 0 is at front of array
    # edge case: where nothing is missing, return next element to be added
    # edge case: empty array
    # loop through arr
    for i in range(len(arr) - 1):
        if len(arr) == 0:
            return
        elif arr[0] != 0:
            return 0
        elif arr[i + 1] != arr[i] + 1:
            return arr[i] + 1
    return arr[-1] + 1


print(find_smallest_missing([0, 1, 2, 4, 5]))
print(find_smallest_missing([1, 2, 3, 5, 6]))
print(find_smallest_missing([0, 1, 2, 3, 4]))
print(find_smallest_missing([]))


# check adjacent elements
# make sure adjacent element == current + 1
