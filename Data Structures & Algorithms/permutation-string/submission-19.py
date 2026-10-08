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

    def compare_counters(self, a: dict, b):
        a_keys = [k for k, v in a.items() if v > 0]
        b_keys = [k for k, v in b.items() if v > 0]
        for key in a_keys + b_keys:
            if a[key] != b[key]:
                return False
                
        return True 

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_counts = Counter(s1)
        window_counts: dict[str, int] = defaultdict(int)
        for k, v in Counter(s2[0:len(s1)]).items():
            window_counts[k] = v

        if window_counts == s1_counts:
            return True 

        prev = 0
        for i in range(len(s1), len(s2)):
            print(f"{i=} {s1_counts=} {window_counts=}")
            window_counts[s2[prev]] -= 1 # drop prev first char out
            window_counts[s2[i]] += 1 # add next char in
            
            if self.compare_counters(window_counts, s1_counts):
                return True 

            prev += 1 

        
        return False




        