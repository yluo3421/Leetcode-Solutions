class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        I need an array to store all of the valid parentheses
        Start from the leftmost bracket in the sequence
        we use left_count and right_count that represent the number of 
        left and right parenthese we have added to our express till 
        current index.
        If the current char s[i] is neither a cloasing or an opening parenthesis
        then we simply add this char to the array
        If the curr char is either of the two brackets
        S[i] == "(" or s[i] == ")"
        We can either discard this char by marking it an invalid char or
        we can consider this bracket to be part of the final answer
        After we went through all expression, we check if the curr answer 
        is valid or not by looking at the left_count and right_count
        if they are left_count == right_count it is valid
        Even thought we find one possible answer, we still need to keep
        trakc of the number of removals we did to get this answer.
        rem_count will do this job.
        Once recursion finishes we check if the current value of rem_count
        is less than the least number of step we had. If it is, record
        the answer.
        
        """
        self.longest_string = -1
        self.res = set()
        
        # string, cur_idx, cur_res, left_count, right_count
        self.dfs(s, 0, [], 0, 0)

        return self.res
    
    def dfs(self, string, cur_idx, cur_res, l_count, r_count):
        if cur_idx >= len(string):
            if l_count == r_count:
                if len(cur_res) > self.longest_string:
                    self.longest_string = len(cur_res)

                    self.res = set()
                    self.res.add("".join(cur_res))
                elif len(cur_res) == self.longest_string:
                    self.res.add("".join(cur_res))
        
        else:
            cur_char = string[cur_idx]

            if cur_char == "(":
                cur_res.append(cur_char)
                # taking cur_char
                self.dfs(string, cur_idx + 1, cur_res, l_count + 1, r_count)

                # not taking cur_char
                cur_res.pop()
                self.dfs(string, cur_idx + 1, cur_res, l_count, r_count)

            elif cur_char == ")":
                self.dfs(string, cur_idx + 1, cur_res, l_count, r_count)

                # checking of l_count should be greater than r_count
                if l_count > r_count:
                    cur_res.append(cur_char)
                    # taking )
                    self.dfs(string, cur_idx + 1, cur_res, l_count, r_count + 1)

                    # not taking )
                    cur_res.pop()
            
            else: # this is for any character except "(" and ")"
                cur_res.append(cur_char)
                self.dfs(string, cur_idx + 1, cur_res, l_count, r_count)
                cur_res.pop()
