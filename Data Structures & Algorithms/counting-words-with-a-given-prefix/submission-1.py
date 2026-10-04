
class TrieNode:
    def __init__(self):
        self.word: bool = False
        self.prefix_count: int = 0
        self.children: dict[str, TrieNode] = {}
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.prefix_count += 1
        
        curr.word = True
    
    def getPrefixCount(self, prefix: str) -> int:
        curr = self.root
        for c in prefix: 
            if c not in curr.children:
                return 0
            
            curr = curr.children[c]
        
        return curr.prefix_count
        

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # return len([w for w in words if w.startswith(pref)])

        t = Trie()
        for word in words:
            t.insert(word)
        
        return t.getPrefixCount(pref)



