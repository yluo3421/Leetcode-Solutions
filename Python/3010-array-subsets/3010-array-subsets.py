from operator import itemgetter


class Solution:
    def findSubsets(n: int, arr: List[int])-> List[int]:
        # thoughts:
        # finding two arrays that union is the original set
        # meaning A + B = arr
        # while A has to be minimal size 2
        # not sure if A has to be size 2,  can be size 2 or larger
        # ** understand that wants to find satisfied A with minimal number of elements
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
        # 
        # To avoid duplicates problem, I have to treat them as one
        # That is to say, I have to put all duplicates together into A
        # Or they will stay in B
        #     
        # so I could find all combinations with quantity of two items
        # find out the combinations that satisfy the requirments
        # then find all combinations with quantity of three items
        # four items, five item until all items
        # [3,7,5,6,2]
        # [3,7]False [3,5]False [3,6]False [3,2]False
        # [7,5]True [7,6]True [7,2]False
        # [5,6]False [5,2]False
        # [6,2]False
        # since we found combinations that satisfy no need to go
        # further to three items

        # try the one with duplicates
        # [2,3,5,5,10]
        # [2,3]False [2,5]False [2,10]False
        # [3,5]False [3,10]True
        # [5,10]False

        # try to generate an example that needs three items
        # [2,3,4,5,5,10]
        # [2,3]False [2,4]False [2,5]False [2,10]False
        # [3,4]False [3,5]False [3,10]False
        # [4,5]False [4,10]False
        # [5,5]False [5,10]False
        
        # [2,3,4]False [2,3,5]False [2,3,10]True
        # [2,4,5]False [2,4,10]true
        # [2,5,5]False [2,5,10]False
        # [3,4,5]False [3,4,10]True
        # [3,5,5]False [3,5,10]False
        # [4,5,5]False [4,5,10]False
        # [5,5,10]True
        # the output should be [5,5,10]
        # one possible way to reduce calculation is to use the two items
        # results in finding the third element
        


        pass
