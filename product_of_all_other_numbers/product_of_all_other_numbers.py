'''
Input: a List of integers
Returns: a List of integers
Write a function that receives an array of integers and returns an array consisting of the product of all numbers in the array _except_ the number at that index. 
'''


def product_of_all_other_numbers(arr):
    # Your code here
    # create arrays to
    length = len(arr)
    l = [0] * length
    r = [0] * length
    t = [0] * length
    l[0] = 1
    for a in range(1, length):
        l[a] = arr[a - 1] * l[a - 1]

    r[length - 1] = 1
    for b in reversed(range(length - 1)):
        r[b] = arr[b + 1] * r[b + 1]

    for c in range(length):
        t[c] = l[c] * r[c]

    return t

    # r = 1
    # for i in arr:
    #     r *= i
    # return [r / n for n in arr]


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
