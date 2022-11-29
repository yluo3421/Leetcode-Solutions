class Solution:
    def compress(self, chars: List[str]) -> int:
        # the idea is to count each char
        # meanwhile we record the group start point by left
        # if its different from the first char of the group
        # then we check how many repeated char we had
        # if count == 1:
        # we assign the prev_char to chars[left]
        # and incresed it by 1
        # if count > 1:
        # we first change count to str so we can add it one by one to 
        # chars
        # after assigning prev_char to chars[left]
        # increased left by 1 and start assigning digit
        # this way left will always keep record of current modification
        # and we will return left for the answer.
        count = 0
        prev_char = chars[0]
        chars.append("")
        
        left = 0
        for char in chars:
            if prev_char == char:
                count += 1
            else:
                if count == 1:
                    chars[left] = prev_char
                    left += 1
                else:
                    count_str = str(count)
                    chars[left] = prev_char
                    left += 1

                    for digit in count_str:
                        chars[left] = digit
                        left += 1
                count = 1
                prev_char = char
        return left