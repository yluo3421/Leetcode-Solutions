class Solution:
    def reverse(self, x: int) -> int:
        # thoughts
        # take all digits one by one and reverse them
        # cannot use str to reverse because the question asked so.
        # to consider oveflow
        # we need to check all steps that might casue overflow
        # temp = ans * 10 + digit > maxInt
        # ans needs to be larger than maxInt/10 so that temp wont go overflow
        # if ans > maxInt/10, then temp always overflow
        # if ans == maxInt/10, then digit needs to be less than 7
        import math
        maxInt = pow(2,31)
        
        ans = 0
        negative = False
        if x < 0:
            x = -x
            negative = True
        while x != 0:
            digit = x % 10
            x /= 10
            if x > 0:
                x = math.floor(x)
            
            if ans > maxInt/10 or (ans == maxInt/10 and digit > 7):
                return 0
            if ans < -maxInt/10 or (ans == maxInt/10 and digit < -8):
                return 0
            
            temp = ans * 10 + digit
            ans = temp
        if negative == True:
            ans = -ans
        
        return ans