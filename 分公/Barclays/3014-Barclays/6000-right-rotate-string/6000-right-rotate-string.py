from re import L


class Solution:
    def right_rotate(word1, word2):
        # thoughts
        # use dict to record both word and then compare
        # this would require O(n) space
        # use two queue to check 
        # the first queue takes word1
        # the seoncd queue takes word2
        # the second queue keep poping left and insert back to 
        # until found queue2 == queue1

        from collections import deque
        if len(word1) != len(word2):
            return -1
        queue1 = deque()
        queue2 = deque()

        for i in range(len(queue1)):
            queue1.insert(word1[i])
            queue2.insert(word2[i])
        
        count = 0
        while count < len(word2):
            curr_char = queue2[0]
            if curr_char == queue1[0]:
                if queue1 == queue2:
                    return 1
                else:
                    curr_char = queue2.popleft()
                    queue2.insert(curr_char)
                    count += 1
        
        return -1
        # O(n*m) Time | O(n) Space

    # second method
    # create a string that is attach word1 to word1
    # if word2 is in this string, return 1

    def temp_string_right_rotate(word1, word2):
        if len(word1) != len(word2):
            return -1
        temp_string = word1 + word1
        if temp_string.count(word2) > 0:
            return 1
        else:
            return -1
    # O(n) Time | O(n) Space

