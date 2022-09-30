def knapsackProblem(items, capacity):
    # Write your code here.
    # each case we could decide whether we take it or not
    # so that with the current package capacity
    # the best result is max of not taking the current item
    # which is the dp value above the current i,j
    # or taking the current item
    # we need to make sure the capacity is enough for this item
    # so we check previous [row] [j - currWeight]
    """
    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - currWeight] + currValue)
    capacity 0 1 2 3 4 5 6 7 8 9 10
    NoItem   0 0 0 0 0 0 0 0 0 0 0
    [1,2]    0 0 1 1 1 1 1 1 1 1 1
    [4,3]    0 0 1 4 4 5 5 5 5 5 5
    [5,6]    0 0 1 4 4 5 5 5 6 9 9
    [6,7]    0 0 1 4 4 5 5 6 6 9 10
    
    """
    # dp representing the max value by this capacity of taking 
    # or not taking the current item
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        [currValue, currWeight] = items[i - 1]
        
        for j in range(1, capacity + 1):
            if j - currWeight >= 0:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - currWeight] + currValue)
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp)
    return [dp[len(items)][capacity], getItemSequence(dp, items)]

def getItemSequence(dp, items):
    sequence = []
    item = len(dp) - 1
    capacity = len(dp[0]) - 1
    while item > 0:
        if dp[item][capacity] == dp[item - 1][capacity]:
            item -= 1
        else:
            sequence.append(item - 1)
            capacity -= items[item - 1][1]
            item -= 1
        if capacity == 0:
            break
    return list(reversed(sequence))