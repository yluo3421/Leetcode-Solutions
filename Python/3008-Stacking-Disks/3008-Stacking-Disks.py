def diskStacking(disks):
    # Write your code here.

    # thoughts
    # sort the disks by height, ascending
    # created dp where
    # dp[i] = max height with this disk as base
    # dp[i] = disks[i] + max(dp[0], dp[1], dp[2]...dp[i - 1])
    #                       in which disks are smaller than the curr

    sorted_disks = sorted(disks, key = lambda x:x[2])
    print(sorted_disks)
    dp = [disk[2] for disk in sorted_disks]
    sequences = [None for _ in range(len(disks))]
    maxHeightIdx = 0
    for i in range(1, len(sorted_disks)):
        currentDisk = sorted_disks[i]
        for j in range(0, i):
            stackDisk = sorted_disks[j]
            if validStack(currentDisk, stackDisk):
                if dp[i] <= currentDisk[2] + dp[j]:
                    dp[i] = currentDisk[2] + dp[j]
                    sequences[i] = j
        if dp[i] >= dp[maxHeightIdx]:
            maxHeightIdx = i
    ans = []
    currentIdx = maxHeightIdx
    while currentIdx is not None:
        ans.append(sorted_disks[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(ans))

def validStack(currentDisk, stackDisk):
    return (
        currentDisk[0] > stackDisk[0]
        and currentDisk[1] > stackDisk[1]
        and currentDisk[2] > stackDisk[2]
           )