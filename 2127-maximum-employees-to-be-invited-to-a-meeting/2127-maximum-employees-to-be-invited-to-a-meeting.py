"""
        There are two ways to fill the table:

some people form a one-way connected cirlce (a -> b -> c -> d -> a, a->b means b is a's favorite people)
some groups of people featured by two mutal-favoriting people (a <-> b, which means both a and b are the other's favorite people)

Here our task is to find out the maximum number of people in these two cases and return the larger one. That is:

The maximum circle in this graph.
The sum of all the longest chain containing all the pairs.

In this problem, each people only has 1 favorite people, which makes this problem easy to handle. We just need to find an unvisited people, mark him/her as visited, find his/her favorite people and go ahead to that person, until we find the first visited people. 
        """
class Solution:
    def maximumInvitations(self, A: List[int]) -> int:
		# First, we find the largest circle.
        n, maxc = len(A), 0
        seen = [0] * n
        for idx in range(n):
		
            # If a people hasn't been visited:
            if seen[idx] == 0:
                
				# start is for locating the first visited people, cur_people stands 
				# for the current people we are visiting, we use curset to store all 
				# the visited people in this iteration.
                start = idx
                cur_people = idx
                curset = set()
				
				# As long as we are visiting new people, we keep finding his/her favorite.
                while seen[cur_people] == 0:
                    seen[cur_people] = 1
                    curset.add(cur_people)
                    cur_people = A[cur_people]
					
				# Until we find the first visited people. Depends on if this 
				# visited people has been visited in eariler iteration or just this iteration.
                if cur_people in curset:       # if current people is in current set, meaning we have found a new circle
                    cursum = len(curset)
					
					# use 'start' to find the distance from the first visited people in this iteration 
					# to this current people.
                    while start != cur_people:
                        cursum -= 1
                        start = A[start]
                    maxc = max(maxc, cursum)
                                       
		# Then we try to find the sum of largest arms. Firstly, find all mutal-favorite peoples.
        pair = []
        visited = [0] * n
        for i in range(n):
		
			# If a is b's favorite and vise versa, we put them in 'pair'.
            if A[A[i]] == i and visited[i] == 0:
                pair.append([i, A[i]])
                visited[i] = 1
                visited[A[i]] = 1
		
		# for every people I, find out all the people whos favorite is I.
        res = 0
        child = collections.defaultdict(list)
        for i in range(n):
            child[A[i]].append(i)
        
        for a, b in pair:
            # max arm length start from first people a
            maxa = 0
            dq = collections.deque()
            for cand in child[a]:
                if cand != b:
                    dq.append([cand, 1])
            while dq:
                cur, n = dq.popleft()
                maxa = max(maxa, n)
                for nxt in child[cur]:
                    dq.append([nxt, n + 1])
                    
            # max arm length start from first people b
            maxb = 0
            dq = collections.deque()
            for cand in child[b]:
                if cand != a:
                    dq.append([cand, 1])
            while dq:
                cur, n = dq.popleft()
                maxb = max(maxb, n)
                for nxt in child[cur]:
                    dq.append([nxt, n + 1])
            
			# Thus the total length is the two longest arm plus 2 (a and b themselves)
            res += 2 + maxa + maxb
			
		# select the larger one as the answer.
        return max(maxc, res)  