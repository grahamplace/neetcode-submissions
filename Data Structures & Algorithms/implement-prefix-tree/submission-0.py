
class TrieNode:
    def __init__(self):
        self.childen = {}
        self.word: bool = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.childen:
                curr.childen[c] = TrieNode()

            curr = curr.childen[c]
        
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c in curr.childen:
                curr = curr.childen[c]
            
        return curr.word 

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c in curr.childen:
                curr = curr.childen[c]
            else:
                return False
        
        return True
            

        