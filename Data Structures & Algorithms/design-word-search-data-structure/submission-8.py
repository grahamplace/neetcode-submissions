from dataclasses import dataclass

@dataclass 
class TrieNode:
    word: bool
    children: dict[str, "TrieNode"]


class WordDictionary:

    def __init__(self):
        self.root = TrieNode(False, {})
    

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(False, {})
                curr = curr.children[c]
            else:
                curr = curr.children[c]

        curr.word = True

    def _search(self, word: str, starting_idx: int, root: TrieNode) -> bool:
        if starting_idx == len(word):
            return root.word 

        if word[starting_idx] == '.':
            # DFS search all the children of current node
            for child_node in root.children.values():
                if self._search(word, starting_idx + 1, child_node):
                    return True
            
            # if no valid children: search not found
            return False
        
        else: # normal character search step
            if word[starting_idx] not in root.children: 
                return False

            return self._search(word, starting_idx + 1, root.children[word[starting_idx]])


    def search(self, word: str) -> bool:
        return self._search(word, 0, self.root) 
