class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # thoughts:
        # 5 101
        # 7 111
        # 2  10
        # 3  11
        # 2  10
        
        # convert all number to binary and then compare the result
        # ans[0] = pref[0]
        # ans[1] = pref[1] / ans[0]
        # ans[2] = pref[2] / ans[1]
        # after trying several numbers realize that bitwise can be calculated reversed
        ans = [pref[0]]
        
        for i in range(1, len(pref)):
            ans.append(pref[i] ^ pref[i - 1])
            
        return ans
            