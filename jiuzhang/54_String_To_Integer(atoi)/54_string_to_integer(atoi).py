class Solution:
    """
    @param s: A string
    @return: An integer
    """
    def atoi(self, str: str) -> int:
        # write your code here
        
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        str = str.strip()
        if str == "" :
            return 0
        i = 0
        sign = 1
        ret = 0
        length = len(str)
        
        if str[i] == '+':
            i += 1
        elif str[i] == '-' :
            i += 1
            sign = -1
        
        for i in range(i, length) :
            if str[i] < '0' or str[i] > '9' :
                break
            ret = ret * 10 + int(str[i])
            if ret > INT_MAX:
                break
        ret *= sign
        if ret >= INT_MAX:
            return INT_MAX
        if ret < INT_MIN :
            return INT_MIN 
        return ret

