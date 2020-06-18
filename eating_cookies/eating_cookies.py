'''
Input: an integer
Returns: an integer
'''


# def eating_cookies(n):
#     # Your code here
#     # runtime: O(c^n) or O(3^n)
#     # base case
#     # for the cases in the tree of possibilities where they equal a negative
#     if n < 0:
#         return 0
#     # for the cases where he eats all the cookies at once
#     elif n == 0:
#         return 1
#     # for the cases with other option combinations
#     else:
#         return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)

# using cache
# cache allows us to save our work, cache is a dictionary where key is the n, value is the answer
# runtime: O(n)
def eating_cookies(n, cache):
    # base case
    # for the cases in the tree of possibilities where they equal a negative
    if n < 0:
        return 0
    # for the cases where he eats all the cookies at once
    elif n == 0:
        return 1
    # checking cache to see if the answer has already been calculated
    elif cache[n] > 0:
        return cache[n]
    # for the cases with other option combinations
    else:
        # otherwise, our cache doesn't contain the answer, so we'll use our recursive logic to calculate it, then save our answer in our cache for future uses
        cache[n] = eating_cookies(
            n-3, cache) + eating_cookies(n-2, cache) + eating_cookies(n-1, cache)
    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 100
    cache = {i: 0 for i in range(num_cookies + 1)}

    print(
        f"There are {eating_cookies(num_cookies, cache)} ways for Cookie Monster to each {num_cookies} cookies")
