class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # record a min so far from the end of the array
        # if the next number is less than min so far
        # counter += 1
        # this method not working because I might encounter 
        # new number to use as start
        
        # I could start from begin
        # whenever smaller number found, that is a new start
        # create a new array
        # but this would create too many arrays
        # to use only one array,
        # use binary search to find the first num in array that is 
        # larger than the lower number
        # [0, 1, 3] found 2
        # binary to find first num that is 3, replace with 2
        # [0,1,2]
        def find_first_larger(array, target):
            left, right = 0, len(array) - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if array[mid] < target:
                    left = mid + 1
                elif array[mid] == target:
                    return mid
                else:
                    ans = mid
                    right = mid - 1
            return ans
        array = []
        for num in nums:
            if len(array) == 0 or array[-1] < num:
                array.append(num)
            else:
                idx = find_first_larger(array, num)
                array[idx] = num
                
        return len(array)
        """
                [4,10,4,3,8,9]
        num           ^
        array   [4,10]
        idx
        """
        