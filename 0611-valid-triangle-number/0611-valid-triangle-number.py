class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        thoughts:
        the brutal force is to go through nums by three times
        find three numbers and make sure they can form a triangle
        That will be O(n^3)
        To optimize this, I think I can sort the source array
        first, this will give me chance to use binary serach.
        Which will improve it to O(n^2log(n))
        Because its sorted, if we found pair (i,j)
        The third one we found that nums[k] > nums[i] + nums[j]
        everyting betweein nums[j+1:k] are all answers
        we can add total count by k - j - 1
        
        Loop of k and j will be executed O(n^2) times in total, 
        because, we do not reinitialize the value of k
        for a new value of j
        chosen(for the same i). Thus the complexity will be 
        O(nlogn + n^2)
        """
        nums.sort()
        count = 0
        for i in range(len(nums) - 2):
            j = i + 1
            k = i + 2
            while j < len(nums) - 1 and nums[i] != 0:
                while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    k += 1
                count += k - j - 1
                j += 1
        return count
        