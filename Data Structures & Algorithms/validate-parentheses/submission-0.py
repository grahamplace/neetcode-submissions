class Solution:
    def isValid(self, s: str) -> bool:
        MAP = {
            "[": "]",
            "{": "}",
            "(": ")",
        }
        open_stack = []
        for c in s:
            if c in MAP:
                # open case, push onto stack
                open_stack.append(c)
            elif c in MAP.values():
                if len(open_stack) == 0 or MAP[open_stack.pop()] != c:
                    return False
            else:
                assert False, "unexpected input char"
        
        return len(open_stack) == 0