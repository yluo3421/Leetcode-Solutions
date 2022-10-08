class Solution:
    def findMaxProduct(arr):
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


        minProduct, maxProduct = 1, 1
        for ele in arr:
            temp = maxProduct
            maxProduct = max(ele * maxProduct, ele * minProduct, ele)
            minProduct = min(ele * temp, ele * minProduct, ele)

