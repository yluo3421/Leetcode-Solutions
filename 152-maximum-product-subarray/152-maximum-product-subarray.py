class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # to find the max product, the brutal force method
        # would require finding all subarrays and calcuulate
        # their products

        # because there might be negative number from the arr
        # we could notice that with one negative times by the curr
        # current max product, it becomes min product
        # [3, 4, -2, 5]
        #  3  12 -24
        # This help me realize that we need to record both max
        # and min value of the current subarray product
        # because min value will become max when negative number
        # occurs.
        # we update min and max for every element
        # new_max = max(ele * maxProduct, ele * minProduct, ele)
        # new_min = min(ele * maxProduct, ele * minProduct, ele)

        # speical case, if we found ele to be 0, max
        # ans is initialized to max of the array cause that will be achieved
        # no matter what
        # if we only update maxProduct, the result will go to 24
        # to solve this we update ans by max(ans, maxProduct)
        
        minProduct, maxProduct = 1, 1
        ans = max(nums)
        for ele in nums:
            temp = maxProduct
            
            maxProduct = max(ele * maxProduct, ele * minProduct, ele)
            print(maxProduct)
            minProduct = min(ele * temp, ele * minProduct, ele)
            ans = max(ans, maxProduct)
        return ans
        