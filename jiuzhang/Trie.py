class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_root(self):
        return self.root
    
    def insert(self, word):
        node = self.root
        # start from root insert each char
        for i in len(word):
            if word[i] not in node.children:
                node.children[word[i]] = TrieNode()
            node = node.children[word[i]]
        node.is_word = True
        node.word = word
    
    # find word corresponding prefix node, return None if not exist
    def find(self, word):
        node = self.root
        for i in range(len(word)):
            node = node.children.get(word[i])
            if node is None:
                return None
        return node
    
    # if the word is complete word in Trie
    def search(self, word):
        node = self.find(word)
        return node is not None and node.is_word
    
    def startsWith(self, prefix):
        return self.find(prefix) is not None
