from _heapq import heapify
'''
Users may input a sentence (at least one word and end with a special character '#').

Given:
sentences: ["i love you", "island", "iroman", "i love neetcode"]
times: [5, 3, 2, 2] (same len as sentences)
- sentences[i] is a previously typed sentence 
- times[i] is the corresponding number of times the sentence was typed

Output: 
For each input character except '#':
return the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed

Rules for "hot sentences":
- The hot degree for a sentence is defined as the number of times a user typedtly the exac same sentence before.
- The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one)
    - If several sentences have the same hot degree, use ASCII-code order (smaller one appears first)
- If less than 3 hot sentences exist, return as many as you can.
- When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list

input(c) continues to build on itself
intput("i") then input(" ") looks up "i "

Example
["i love you", "island", "iroman", "i love neetcode"] / [5, 3, 2, 2]
input("i") => ["i love you", "island", "i love neetcode"] (top 3 hottest of all matches starting w "i")
input(" ") => ["i love you", "i love neetcode"] (top 3 hottest best effort starting with "i ")

IMPORTANT:
- When user finishes input by sending "#", the sentence they just ended should be saved as a historical sentence in system. - - And the following input will be counted as a new search!
'''

from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        # self.sentences: set[str] = set()
        self.top_3_sentences: list[tuple[int, str]] = []

class AutocompleteSystem:

    SIZE = 3

    def __init__(self, sentences: List[str], times: List[int]):
        self.current_query = ""
        self.sentences: dict[str, int] = defaultdict(int)
        self.trie_root = TrieNode()

        for sentence, t in zip(sentences, times):
            self.sentences[sentence] += t
            self._insert_sentence_trie(sentence, t)

    def _add_sentence_to_node(self, sentence: str, times: int, node: TrieNode) -> None:
        candidates = [s for s in node.top_3_sentences if s[1] != sentence]
        candidates.append((times, sentence))
        node.top_3_sentences = sorted(candidates, key=lambda x: (-x[0], x[1]))[:self.SIZE]

    def _insert_sentence_trie(self, sentence: str, times: int) -> None:
        curr = self.trie_root
        for c in sentence:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
            self._add_sentence_to_node(sentence, times, curr)

    def _search_prefix(self, prefix: str) -> list[str]:
        curr = self.trie_root
        for c in prefix:
            if c not in curr.children:
                return []
            
            curr = curr.children[c]

        # now we need ALL sentences below this node in the trie:
        return [x[1] for x in curr.top_3_sentences]


    def _run_query(self, query: str) -> list[str]:
        # we can use Trie to get only the subset of sentences that match this prefix, rather than all N
        matches = self._search_prefix(query)
        #  If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
        return sorted(matches, key=lambda x: (-self.sentences[x], x))[:self.SIZE]

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.sentences[self.current_query] += 1
            self._insert_sentence_trie(self.current_query, self.sentences[self.current_query])
            self.current_query = ""
            return []

        self.current_query += c
        return self._run_query(self.current_query)


obj = AutocompleteSystem(["ab", "ab"], [2, 2])
assert obj._run_query("a") == ["ab"]

obj = AutocompleteSystem(["ab", "ab", "abc"], [2, 2, 10])
assert obj._run_query("a") == ["abc", "ab"]
        






