'''
inputs:
two strings, s1 / s2
- lowercase only 
- <10000 chars

Problem: 
- if a permutation of s1 exists as a substr of s2 
- ex 1 
- "abc" "lecabeee" -> True
- a b and c are in s2 (in any order but must be contiguous)

- ex 2
- "abc" "lecaabeee" -> False
- a b and c are in s2 (broken up)

Output:
- bool
- true if s2 contains a permutation of s1, otherwise false

Idea:

1. Parse s2 into counts O(N) where N is len s1
{
"a": 1
"b": 1
"c": 1
}

2. Step over s2 char by char. (run pointer i)
When s2[i] in s1_counts:
- copy s1_counts for this loop
- start running ptr j forward
- check s2[j] is in s1_counts and count > 0
- if yes, decr count. +1 chars_matched
- if no: 
- if chars_matched == len(s1), return True
- else set i = j and continue
- * Need to handle case where we reach end of string too 



'''
class Solution:

    def check_window(self, s1_counts, s2, i, j) -> bool:
        print(f"{s2[i:j]} {i=} {j=}")
        return Counter(s2[i:j]) == s1_counts

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_counts = Counter(s1)
        for i in range(len(s2) - len(s1) + 1):
            if self.check_window(s1_counts, s2, i, i + len(s1)):
                return True
        
        return False




        