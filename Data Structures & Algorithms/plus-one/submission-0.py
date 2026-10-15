class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        output = []
        i, carry = len(digits) - 1, 1
        while True:
            if i < 0 and carry == 0:
                break

            new_val = digits[i] + carry if i >= 0 else carry
            if new_val < 10:
                output.append(new_val)
                carry = 0
            else:
                
                this_digit = new_val % 10
                output.append(this_digit)
                carry = new_val // 10

            i -= 1

        output.reverse()
        return output
