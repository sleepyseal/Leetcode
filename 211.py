class WordDictionary:
    def __init__(self):
        self.is_end=False
        self.child=[None]*26
    def addWord(self, word):
        node=self
        for i in word:
            character=ord(i)-ord('a')
            if node.child[character] is None:
                node.child[character]=WordDictionary()
            node=node.child[character]
        node.is_end=True
    def search(self, word):
        def dfs_search(node, word, index):
            if index==len(word):
                return node.is_end
            ch=word[index]
            if ch ==".":
                for child in node.child:
                    if child is not None and dfs_search(child, word, index+1):
                        return True
            else:
                ch_index=ord(ch)-ord('a')
                if node.child[ch_index] is not None and dfs_search(node.child[ch_index], word, index+1):
                    return True
            return False
        return dfs_search(self, word, 0)
wordDictionary =WordDictionary()
wordDictionary.addWord("a")
wordDictionary.addWord("a")
wordDictionary.search("a.")
