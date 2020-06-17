'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    
    # separate all zeros in the array here
    ZeroElments = [ 0 for i in range(arr.count(0))]
    #Separate all other elements here.
    otherElements = [i for i in arr if i != 0]

    otherElements.extend(ZeroElments)
    return(otherElements)
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")