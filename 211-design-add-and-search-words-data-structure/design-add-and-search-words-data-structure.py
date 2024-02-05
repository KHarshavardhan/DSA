class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end= True

    def search(self, word: str) -> bool:
    #dfs is depth for search method, this recusive function is used to traverse all option when a "." is present in word instead of a char and if any matching word is found returns True else False
        def dfs(j,root):
            curr = root
            for i in range(j,len(word)):
                c = word[i]
                if c == ".":
                    for d in curr.children.values():
                        if dfs(i+1,d):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        curr.children[c] = TrieNode()
                    curr = curr.children[c]
            return curr.end
        return dfs(0,self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)