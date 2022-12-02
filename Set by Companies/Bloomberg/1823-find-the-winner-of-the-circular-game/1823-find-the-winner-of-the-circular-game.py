class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        """
        counting k friends is to find k % n th friend
        Since everytime one friend will be out of game
        Initial queue = [5, 4, 3, 2, 1]
        k = 2

        Pop and Push k-1 friends to the back of queue
        [1, 5, 4, 3, 2]

        Pop front element
        [1, 5, 4, 3] --> 2 (looses)

        Repeat
        [3, 1, 5, 4]
        [3, 1, 5] --> 4

        [5, 3, 1]
        [5, 3] --> 1

        [3, 5]
        [3] --> 5

        Winner 3!!
        """
        queue = list(range(n, 0, -1))    #Creates list of n to 1
        cur_k = k - 1
        while len(queue) != 1:
            while cur_k != 0:
                queue.insert(0, queue.pop())    #Popping front element and pushing it to the end of queue
                cur_k -= 1
            queue.pop()      #Popping the friend that looses
            cur_k = k - 1    #Resetting
        
        return queue.pop()   #Winner
        
        