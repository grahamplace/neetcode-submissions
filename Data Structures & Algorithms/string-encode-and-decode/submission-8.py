class Solution:
    DELIM = "#"

    def encode(self, strs: List[str]) -> str:
        output = []
        for s in strs:
            encoded = f"{self.DELIM}{len(s)}{self.DELIM}{s}"
            output.append(encoded)

        return ''.join(output)

    def decode(self, s: str) -> List[str]:
        output, i = [], 0

        while i < len(s):
            if s[i] == self.DELIM:  # First delim starts the count string of the next string
                j, count_str = i + 1, ""
                while j < len(s):
                    if s[j] == self.DELIM:  # Next delim ends the count string
                        break
                    else:
                        count_str += s[j]
                    j += 1

                word_len = int(count_str)
                word_end = j + word_len + 1
                output.append(s[j + 1 : word_end])
                i = word_end  # Continue on from the char following the end of this word

        return output
