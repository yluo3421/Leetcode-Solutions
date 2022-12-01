# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        """
        thoughts
        first comes to me that we have 400 calls and with
        grid width of 1000 we cannot solve this to traverse
        all points. Maybe we can divide them into half and 
        half to check
        Maybe we should try divided into 4 since it specifically
        said Caresian plane.
        This sounds like a brutal force way
        We will first check the current one has oneShip
        If yes, divided into 4 by taking the mid point and check
        if they has one Ship again. Recursively find total number of ships
        If none of them has ship we will take out those 
        rectangles that doesnt have ship

        If we are using 4 division, total we have 1,000,000 points
        to visit, we need to divide 
        its 2^2 by how many times
        can I check this online? Even though I am Chinese I am not
        good at math.
        Ok I found its about 10 times
        so 4^10 to be checked, that is still a lot.
        So time complexity is 4^10, is this okay to proceed?
        I want to confirm if this is the approach you would like to see

        Wait the actual complexity wont be that bad
        because it is only 10 ships maximum. In that case, 
        Even though we might have 4^level rectangels to check
        But eventually only 10 with ship will be passed to next level
        so time complexity should be 
        number of ships * 4 *number of levels log4(1,000,000) = 10
        10*4*10 = 400
        First time I got such a specific time complexity

        """
        # the way we divided into 4
        #                               mid_x, topRight.y                          topRight.x, topRight.y
        # bottomLeft.x, mid.y + 1                      mid.x + 1, mid.y + 1
        #                               mid.x, mid.y                                topRight.x, mid.y
        # bottomLeft.x, bottomLeft.y                  mid.x + 1, bottomLeft.y

        # recurssion stops when it cannot be divided anymore
        if bottomLeft.x > topRight.x or bottomLeft.y > topRight.y:
            return 0
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        
        # rectangle is only one single point meaning its the ship
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1
        
        mid_x = (topRight.x + bottomLeft.x) // 2
        mid_y = (topRight.y + bottomLeft.y) // 2
        mid = Point(mid_x, mid_y)
        return self.countShips(sea, mid, bottomLeft) + \
            self.countShips(sea, topRight, Point(mid_x + 1, mid_y + 1)) + \
            self.countShips(sea, Point(mid_x, topRight.y), Point(bottomLeft.x, mid_y + 1)) + \
            self.countShips(sea, Point(topRight.x, mid_y), Point(mid_x + 1, bottomLeft.y))
        