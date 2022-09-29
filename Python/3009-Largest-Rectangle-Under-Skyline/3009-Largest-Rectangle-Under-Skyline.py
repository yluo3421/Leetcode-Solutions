class Solution:
    def largestRectangleUnderSkyline(self, buildings):
    # Write your code here.
    # thoughts:
    # brutal force:
    # check all possible rectangles
    if len(buildings) == 0:
        return 0
    if len(buildings) == 1:
        return buildings[0]
    if len(buildings) == 2:
        max_height = max(buildings[0], buildings[1])
        min_height = min(buildings[0], buildings[1])
        return max(max_height, min_height * 2)
    # when there is three or moe of them.
    # check each building to their left and right, how far they can go.
    maxArea = 0
    for i in range(len(buildings)):
        currHeight = buildings[i]
        max_width = self.checkLeftAndRight(buildings, i)
        maxArea = max(maxArea, max_width * currHeight)
        # maxArea.append(max_width * currHeight)
    
    return maxArea
    

def checkLeftAndRight(self, buildings, currIdx):
    left = currIdx - 1
    right = currIdx + 1
    currHeight = buildings[currIdx]
    while left >= 0:
        if buildings[left] >= currHeight:
            left -= 1
        else:
            break
    left = max(0, left + 1)

    while right < len(buildings):
        if buildings[right] >= currHeight:
            right += 1
        else:
            break
    right = min(right - 1, len(buildings) - 1)
    # print(left)
    print(left, right)
    return right - left + 1
        
            
    

        
