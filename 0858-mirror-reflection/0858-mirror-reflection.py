class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        """
        we need to find the n * p = m * q
        because if we stack more glass box on top of this one
        let the light go through the top mirror
        At the end when light hit one of the receptor
        |       |
        |       |_
        |_      |
        |       |_
        |       |
        |_      |_
        on the example above we have 2p and on right we have 3q
        and its acutally hitting recptor 0
        1p = 3q output 1
        1p = 2q output 2
        2p = 3q output 0
        we can tell that
            m       n       output
            odd     even    2
            odd     odd     1
            even    odd     0
        thus we need to find the lowest common multiple
        If p and q are both even, they are the multiples of 2, so we can divide p and q by 2 to reduce our equation.
        for example p = 2*2*x q = 2*2*y
        m*p = n*q => m*(2*2*x) = n*(2*2*y)
                    => m*x = n*y
        If p is even then q is odd, and because m*p = n*q then n should be even
        numer of reflecting times is even means the ray ends at the top-left corner which could be only the corner 2
        
        If q is even then p is odd, and because m*p = n*q then m should be even
=> the number of stacked boxes is even means the current box is the flipped version of the original box so the top-right corner should be only 0

        else, it ends at 1
        
        
        Space Complexity is obviously O(1)
        Time Complexity is O(min(log(p), log(q)) 
        but because q <= p so the worst case is only : O(log(q))
        """
        while p % 2 == 0 and q % 2 == 0:
            p = p / 2
            q = q / 2
	    
        if p % 2 == 0:
            return 2
        if q % 2 == 0:
            return 0
        return 1