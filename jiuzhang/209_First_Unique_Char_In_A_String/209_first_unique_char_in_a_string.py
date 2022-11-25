class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def first_uniq_char(self, str: str) -> str:
        # Write your code here
        # method 2
        # push (char, i) into queue
        # dict to record {char: freq} if char exist, make freq -1 meaning duplicates
        # while queue[0] char in posistion is -1, pop out
        # retrun q[0][0]
        position = dict()
        q = collections.deque()
        n = len(str)
        for i, ch in enumerate(str):
            if ch not in position:
                position[ch] = i
                q.append((str[i], i))
            else:
                position[ch] = -1
                while q and position[q[0][0]] == -1:
                    q.popleft()
        return ' ' if not q else q[0][0]


        # go through the array and use a set to record
        freq_dict = collections.Counter(str)
        for char in str:
            if freq_dict[char] == 1:
                return char
        
        
            
            
        
        
        