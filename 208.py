class Trie:
    def __init__(self):
        self.is_end=False
        self.child=[None]*26
    def search_prefix(self, prefix):
        node=self
        for i in prefix:
            character=ord(i)-ord('a')
            if node.child[character] is None:
                return None
            node=node.child[character]
        return node
    def insert(self, word):
        node=self
        for i in word:
            character=ord(i)-ord('a')
            if node.child[character] is None:
                node.child[character]=Trie()
            node=node.child[character]
        node.is_end= True
    def search(self, word):
        node=self.search_prefix(word)
        if node is not None and node.is_end:
            return True
        return False
    def startsWith(self, prefix):
        node=self.search_prefix(prefix)
        if node:
            return True
        return False
trie = Trie()
trie.insert("apple")
trie.search("apple")
trie.search("app")
trie.startsWith("app")
trie.insert("app")
trie.search("app")
        