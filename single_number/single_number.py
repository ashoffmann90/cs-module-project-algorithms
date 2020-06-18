'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here
    # check if there is a duplicate by using count
    # MY CODE
    # for i in arr:
    #     c = arr.count(i)
    #     if c == 1:
    #         return i
    c = [i for i in arr if arr.count(i) == 1]
    return c[0]

    # could also use contains???

    # # SEAN'S CODE
    # # use either dictionary or set
    # s = set()
    # # sets good for: holding on to unique elements
    # # loop through arr
    # for i in arr:
    #     # for each element
    #     # check if it is already in set
    #     # if it is, then that's not our odd element out
    #     if i in s:
    #         s.remove(i)
    #     else:
    #         s.add(i)
    # # remove the element from our set
    # return list(s)[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
