class Solution:
    def find_gcd_n_numbers(arr):
        # thoughts:
        # find gcd of the frist two numbers
        # use this gcd to find gcd of (curr_gcd, next num)

        # Euclidean
        # the wont change if smaller number is subtracted from larger number
        # use % we can minus smaller number from the larger number
        # until b is 0
        # at that time a is the gcd
        def find_gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        num1 = arr[0]
        num2 = arr[1]
        curr_gcd = find_gcd(num1, num2)
        for i in range(2, len(arr)):
            curr_gcd = find_gcd(curr_gcd, arr[i])
        return curr_gcd
        # O(n * log(n)) Time where n is the lagest number in arr