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

class AutocompleteSystem:

    SIZE = 3

    def __init__(self, sentences: List[str], times: List[int]):
        self.current_query = ""
        self.sentences: dict[str, int] = defaultdict(int)

        for sentence, t in zip(sentences, times):
            self.sentences[sentence] += t

    def _run_query(self, query: str) -> list[str]:
        matches = [s for s in self.sentences if s.startswith(query)]
        #  If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
        return sorted(matches, key=lambda x: (-self.sentences[x], x))[:self.SIZE]

    def input(self, c: str) -> List[str]:
        if c == '#':
            pass # flush to sentences 
            self.sentences[self.current_query] += 1
            self.current_query = ""
            return []

        self.current_query += c
        return self._run_query(self.current_query)


obj = AutocompleteSystem(["ab", "ab"], [2, 2])
assert obj._run_query("a") == ["ab"]

obj = AutocompleteSystem(["ab", "ab", "abc"], [2, 2, 10])
assert obj._run_query("a") == ["abc", "ab"]
        






