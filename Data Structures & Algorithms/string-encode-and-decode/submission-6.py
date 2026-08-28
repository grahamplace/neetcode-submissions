class Solution:

    DELIM = '#'

    def encode(self, strs: List[str]) -> str:
        output = ''
        for s in strs: 
            encoded = f'{self.DELIM}{len(s)}{self.DELIM}{s}'
            output += encoded
        
        return output

    def decode(self, s: str) -> List[str]:
        output, i = [], 0

        while i < len(s):
            if s[i] == self.DELIM:
                j = i + 1
                count_str = ''
                while j < len(s):
                    if s[j] == self.DELIM:
                        break
                    else:
                        count_str += s[j]
                    j += 1

                i_len = int(count_str)
                output.append(s[j+1:j+i_len+1])
                i = j + i_len + 1
            
        return output

            

