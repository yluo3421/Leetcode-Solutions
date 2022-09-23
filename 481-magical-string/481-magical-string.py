class Solution:
    def magicalString(self, n: int) -> int:

        """
        @param n: an integer 
        @return: the number of '1's in the first N number in the magical string S
        """
    
    
    
        # write your code here
        #         1 2 2 1 1 2 1 2 2 1 1 2 1 1 2 2 
        # currNum           ^ step+occur
        # occur.        ^ occur += 1
        #.        1 2 2 1 1 
        # occur.  1 2 2 1 1 2 1 2 2
        oneOrTwo = True
        count = 0
        occur = 0
        magical_string = ""
        i = 0
        while len(magical_string) < n:
            if oneOrTwo:
                currentNum = "1"
                magical_string += currentNum
                occur = 2 if magical_string[i] == "2" else 1
                if occur == 2:
                    magical_string += currentNum
                count += occur
                oneOrTwo = not oneOrTwo
                
            else:
                currentNum = "2"
                magical_string += currentNum
                occur = 2 if magical_string[i] == "2" else 1
                if occur == 2:
                    magical_string += currentNum
                oneOrTwo = not oneOrTwo
            i += 1
        print(magical_string)
        if len(magical_string) == n:
            return count
        else:
            return count - 1 if magical_string[-1] == "1" else count
        return count