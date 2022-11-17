from typing import (
    List,
)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        # 从当前前缀节点向下的最大高度
        self.max_height = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def get_root(self):
        return self.root
    
    def insert(self, word):
        node = self.root

        for i, c in enumerate(word):
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.max_height = max(node.max_height, len(word) - i - 1)
        node.is_word = True

class Solution:
    """
    @param s: the list of binary string
    @return: the max distance
    """
    def get_ans(self, s: List[str]) -> int:
        trie = Trie()
        for word in s:
            trie.insert(word)
        return self.dfs(trie.get_root())
    
    def dfs(self, root):
        result = 0
        # 最大距离可能性一：如果在此处分叉，考虑两个分支的最大高度之和
        if len(root.children) == 2:
            # 这里要加2，需要吧root的左右孩子各有一条边算进去
            result = max(result,
                        root.children["0"].max_height + \
                        root.children["1"].max_height
            ) + 2
        # 最大距离可能性二：如果当前root是完整的词，考虑root的最大高度
        if root.is_word:
            result = max(result, root.max_height)
        # 最大距离可能性三：如果当前root有0分支，考虑0分支这可子树中的最大距离
        if "0" in root.children:
            result = max(result, self.dfs(root.children["0"]))
        # 最大距离可能性四：如果当前root有1分支，考虑1分支这可子树中的最大距离
        if "1" in root.children:
            result = max(result, self.dfs(root.children["1"]))
        # 四种可能性中最大的就是result
        return result