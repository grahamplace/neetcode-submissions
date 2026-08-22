'''
Given two strings text1 and text2:
-> return the length of the longest common subsequence between the two strings (if one exists)
-> if no common subsequence, return 0

? subsequence
-> a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.
--> "cat" is a subsequence of "crabt". (remove r, remove b)

? common subsequence
-> a subsequence that exists in both strings

inputs: 
- text1, text 2: both short strings
- inputs are between 1 and 1000 chars
- No empty strings allowed
- lowercase Eng chars only - don't need to normalize

examples:

1. (answer 3)
text1 = "cat"
text2 = "crabt" 

- step 1: what are my possible actions?
- "deleting some or no elements"
- I could delete from text1
- I could delete from text2
- If either is empty string, then I can't delete
- If both are len 1, and they are =, that is a common subsequence


if I start at char 0 of text 1, and I iterate over text2, and I never find text1[0], then I should remove it from text 1 
note: order DOES matter since we're dealing with subSEQUENCEs
you could think of each word as a DAG. first char is connected to all subsequent chars

cat 
crabt

start small
L(c, c) = c : 1
L(ca, cr) = c : 1
 -> if next chars don't match, then L(ca, cr) = L(c, c)
L(cat, cra) = c : 1

We shouldn't vary length at the same time
you could imagine a 2d array where one dim is prefix of text1 and other is text 2, cell value is longest common
-> at the bottom right is our solution

'''



class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        prefix_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            prefix1 =  text1[:i + 1]
            for j in range(cols):
                prefix2 =  text2[:j + 1]
                if prefix1[-1] == prefix2[-1]:
                    if i == 0 or j == 0:
                        new_value = 1
                    else:
                        new_value = prefix_matrix[i - 1][j - 1] + 1

                    prefix_matrix[i][j] = new_value
                    row_has_matched = True

                else:
                    above = prefix_matrix[i - 1][j] if i > 0 else 0
                    left = prefix_matrix[i][j - 1] if j > 0 else 0
                    prefix_matrix[i][j] = max(above, left)

        return prefix_matrix[-1][-1]






















