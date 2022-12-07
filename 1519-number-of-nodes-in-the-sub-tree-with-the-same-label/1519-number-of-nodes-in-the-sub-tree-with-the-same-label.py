class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        """
        Brutal force
        use dfs to explore every subtree of every node
        and count how many similar in there.
        Time complexity will be O(n^2)
        Is this what you are looking for?
        To optimize this, we can record one node's child nodes'
        situation, and use them to calcuulate parent node
        
        1. create adjacent_list useing edges
        2. use ans array for each node, intialize 0
        3. dfs(node, parent, adj_list, labels, ans) returns an array
        which stores the count of each label in the node's subtree
        
        Initialize an array nodeCounts to 
        store the count of each label in the node's subtree. 
        Initialize it with 0 except for the node label, which should be 1.
        
        Iterate over all the children of the node (nodes that 
        share an edge) and check if any child is equal to the 
        parent. If the child is equal to the parent, we will 
        not visit it again.
        
        If the child is not equal to the parent, recursively 
        call the dfs function with the node as child and the 
        parent as node. Store the count of all labels in its 
        subtree in childCounts.
        
        Add childCounts to nodeCounts.
        """
        
        def dfs(node: int, parent: int):
            cnt = Counter(labels[node])
            for child in adjacent_list.get(node, []):
                if child != parent:
                    cnt += dfs(child, node)
            ans[node] = cnt[labels[node]]
            return cnt

        adjacent_list, ans = defaultdict(list), [0] * n
        for a, b in edges:
            adjacent_list[a] += [b]
            adjacent_list[b] += [a]
        dfs(0, -1)
        return ans   