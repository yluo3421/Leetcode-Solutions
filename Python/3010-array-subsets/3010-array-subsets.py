class Solution:
    def findSubsets(n: int, arr: List[int])-> List[int]:
        # thoughts:
        # finding two arrays that union is the original set
        # meaning A + B = arr
        # while A has to be minimal size 2
        # not sure if A has to be size 2,  can be size 2 or larger
        # either case the brutal force will be sort the original arr
        # add the max two number and check if A satisifies all condition
        #
        # the drawback of this method is it cannot take duplicates
        # for example arr = [2,3,5,5,10]
        # that the A found will be [10, 5]
        # but B will be [2,3,5] where A and B has intersecitno of 5
        # the correct A should be [10, 3]

        # more brutal force
        # check all combinations of A
        # find the max sum of A that still satisfies all requriments
        # how do I find all combinations of A
        # sum of A = elements picked
        # sum of B = sum of all - sum of A     
        pass
