'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
Given an array of integers, there is a sliding window of size `k` which is moving from the left side of the array to the right, one element at a time. You can only interact with the `k` numbers in the window. Return an array consisting of the maximum value of each window of elements.
'''


def sliding_window_max(nums, k):
    # Your code here
    # init empty arr and append max vals to each window
    max_vals = []
    # loop through nums arr from k to len(nums) +1
    for num in range(k, len(nums) + 1):
        # create window from num - k to num
        window = nums[num - k:num]
        max_vals.append(max(window))
    # return max vals
    return max_vals

    # one liner
    # [max(nums[num - k: num]) for num in range(k, len(nums) + 1)]


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
