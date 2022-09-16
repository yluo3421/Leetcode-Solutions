def sortedSquaredArray(array):
    # Write your code here.
    # thoughts
    # use two pointer from both ends, the one with larger absolute value
    # will be added to the end of the array
    # the two pointer goes into the middle
    sortedSquare = [0 for _ in range(len(array))]
    smallerIndex, largerIndex = 0, len(array) - 1
    for i in reversed(range(len(array))):
        smallerValue = abs(array[smallerIndex])
        largerValue = abs(array[largerIndex])
        if smallerValue > largerValue:
            sortedSquare[i] = smallerValue * smallerValue
            smallerIndex += 1
        elif smallerValue <= largerValue:
            sortedSquare[i] = largerValue * largerValue
            largerIndex -= 1
    return sortedSquare
    # O(N) Time | O(N) Space

    # It is ok to simply give new array the square of current item
    # but eventually I have to sort, and it will take O(nlog(n)) Time
    """
    def sortedSquaredArray(A):
    
    for i in range(len(A)):
            A[i] *= A[i]
    A.sort()
    return A
    """