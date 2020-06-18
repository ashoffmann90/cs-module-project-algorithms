# def find_smallest_missing(arr):
#     # edge case: where 0 is missing, make sure 0 is at front of array
#     # edge case: where nothing is missing, return next element to be added
#     # edge case: empty array
#     # loop through arr
#     for i in range(len(arr) - 1):
#         if len(arr) == 0:
#             return
#         elif arr[0] != 0:
#             return 0
#         elif arr[i + 1] != arr[i] + 1:
#             return arr[i] + 1
#     # last case: where nothing is missing, so we return what would come next
#     # O(n)
#     return arr[-1] + 1


def find_smallest_missing(arr):
    # is there a possibility of using binary search for this problem?
    # with binary search, we need to know our target element
    # the smallest element is the first element that doesn't match it's index
    # can we use binary search to find this element
    low = 0
    high = len(arr) - 1
    if len(arr) == 0:
        return 0
    # use binary search, except we'll check the midpoint element, we're checking to see if the value matches the index itself

    while low < high:
        mid = (low+high)//2
    # if it does, the smallest missing element could still occur after this point, so we'll cut out the left half
        if arr[mid] == mid:
            # check adjacent element to see if it's the smallest missing
            if arr[mid + 1] != arr[mid] + 1:
                return arr[mid] + 1
            # update our low variable
            low = mid + 1

    # if it doesn't, either the midpoint is the smallest missing element, or the smallest missing happened earlier to the left, so we cut out the right side
        else:
            high = mid

    # continue this process until we narrow it down to either one element, or the low and the high indicces surpass one another

    # if we don't find anything by the end of the loop, then there was no smalllest missing element and we return the element that would come next
    return high


print(find_smallest_missing([0, 1, 2, 4, 5]))
print(find_smallest_missing([1, 2, 3, 5, 6]))
print(find_smallest_missing([0, 1, 2, 3, 4]))
print(find_smallest_missing([]))
