'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    
    # check for 0's in array.
    zeros = [0 for i in range(arr.count(0))]
    print(zeros)
    # separate remain elements from the 0.
    non_zeros = [i for i in arr if i != 0]
    non_zeros.extend(zeros)
    return non_zeros
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")