class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }

        stack = []
        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                stack.append(operators[token](a, b))

            else:
                stack.append(int(token))

        return stack[0]