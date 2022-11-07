class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """
    def k_distinct_characters(self, s: str, k: int) -> int:
        # Write your code here
        str_len = len(s)
        num_of_substrings = 0

        # the number of unique letters between two pointers
        num_of_unique_letters = 0
        letter_counter = [0] * 26 # both dict and array can help here
        end = 0

        for start in range(str_len):
            # find the closest end pointer that there are k
            # distinct chars between two pointers
            while end < str_len and num_of_unique_letters < k:
                end_letter_index = ord(s[end]) - ord("a")
                letter_counter[end_letter_index] += 1
                # if char at end pointer is the first time occurs
                # update the unique char count
                if letter_counter[end_letter_index] == 1:
                    num_of_unique_letters += 1
                end += 1
            
            # confirm there is k unique chars
            # all substring ended between end pointer and end of string
            # are valid canditates should be added to num of substrings
            if (num_of_unique_letters == k):
                num_of_substrings += str_len - end + 1
            
            # move start pointer with the for loop 
            start_letter_index = ord(s[start]) - ord("a")
            letter_counter[start_letter_index] -= 1
            # after start pointer move
            # if the current char get 0, update unique count
            if letter_counter[start_letter_index] == 0:
                num_of_unique_letters -= 1
        
        return num_of_substrings