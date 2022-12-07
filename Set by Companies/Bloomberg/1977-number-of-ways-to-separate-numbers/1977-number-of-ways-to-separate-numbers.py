class Solution:
    def __init__(self):
        self.memo = { }
        self.MOD = 1000000007
    def partition(self, n):
        if n == 0: return 1
        if n in self.memo: return self.memo[n]
        v = 0
        k = 1
        while n >= k * (3 * k - 1) // 2:
            sub = n - k * (3 * k - 1) // 2
            v = int(v - self.partition(sub) * ((-1) ** k)) % self.MOD
            if k > 0:
                k *= -1
            else:
                k = 1 - k
        self.memo[n] = v
        return v
    def numberOfCombinations(self, num: str) -> int:
        if num[0] == '0':
            return 0
        if len(Counter(num)) == 1:
            return self.partition(len(num))
        @cache
        def sep(i=-1,j=-1):
            if j > -1 and num[i] == '0':
                return 0
            s = j + 1
            if s == len(num):
                return 1
            e = s + (j - i)
            if e >= len(num):
                return 0
            if j > -1 and num[i:j+1] > num[s:e+1]:
                e += 1
            c = 0
            while e < len(num):
                c += sep(s,e)
                e += 1
            return c % self.MOD
        return sep()
        """
        Let us start as many other solutions with the 
        following idea. Let dp[i][k] be the number of 
        solutions for string s[:i] (not including) such 
        that the last element has length k. How we can 
        get dp[i][k]? 
        We need to look at dp[i-k][1], ..., dp[i-k][k-1] 
        and probably at dp[i-k][k]. Can we take the 
        last one or not depends on comparison of two 
        k-digit strings. Let us for the moment forgot 
        about this and talk about how to find dp[i][k] efficiently.

        We notice, that we need co calculate cumulative 
        sums dp[i-k][1], ..., dp[i-k][k-1], so it is 
        good idea keep them as well: by definition

        mp[i][k] = dp[i][1] + ... + dp[i][k]. Then we 
        can say that what we need to find is mp[i-k][k]. 
        So far, so good, but what to do with comparison 
        of strings. It is quite expensive and as we will 
        see a bit later we can allow to make this 
        comparison only in O(1) (or probably in O(log n) in other languages.

        For this we want to use suffix array. What it is?

        Let us consider for simplicity example banana. Then what we want to construct is list of all suffixes: banana, anana, nana, 
        ana, na, a and then sort them in increasing order:
        we have a, ana, anana, banana, na, nana. Actually what we keep is order if indexes: (5, 3, 1, 0, 4, 2), this is called suffix array. 
        After we comput prefix array, we can check strings just in O(1). 

        

        Complexity
        Time complexity of suffix array part is O(n*log^2n) 
        and it is quite fast and tested by me in some other problems. 
        Time complexity of dp part is O(n^2), because we have 
        n states for i and not more than n for j. Notice however 
        that we have quite expansive comparison function: 
        it is O(1), but we do a lot of indexing which is quite 
        slow in python. So, verdict is TLE on the last test.
        """
        
        def ranks(l):
            index = {v: i for i, v in enumerate(sorted(set(l)))}
            return [index[v] for v in l]

        def suffixArray(num):
            line = ranks(num)
            n, k, ans, sa = len(num), 1, [line], [0]*len(num)
            while k < n - 1:
                line = ranks(list(zip_longest(line, islice(line, k, None), fillvalue=-1)))
                ans, k = ans + [line], k << 1
            for i, k in enumerate(ans[-1]): sa[k] = i
            return ans, sa

        @lru_cache(None)
        def compare(i, j, l, k):
            a = (c[k][i], c[k][(i+l-(1<<k))%n])
            b = (c[k][j], c[k][(j+l-(1<<k))%n])
            return 0 if a == b else 1 if a < b else -1

        c, _ = suffixArray([int(i) for i in num])

        n, M = len(num), 10**9 + 7
        dp = [[0]*(n+1) for _ in range(n+1)]
        mp = [[0]*(n+1) for _ in range(n+1)]

        for k in range(n+1):
            dp[0][k] = 1
            mp[0][k] = 1

        for i in range(1, n+1):
            for k in range(1, i + 1):
                if num[i-k] == "0": continue
                dp[i][k] = mp[i-k][k-1]
                if i >= 2*k and compare(i-2*k, i-k, k, floor(log2(k))) >= 0:
                    dp[i][k] += dp[i-k][k]

            for k in range(n + 1):
                mp[i][k] = mp[i][k-1] + dp[i][k]

        return mp[-1][-1]