class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1: return int(tokens[0])
        def evaluate(sign, y, x):
            x = int(x)
            y = int(y)
            if sign == '+':
                return x + y
            elif sign == '-':
                return x - y
            
            elif sign == "*":
                return x * y
            else:
                return int(x/y)
        
        stack = []

        for t in tokens:
            stack.append(t)
            if t in "+-*/":
                val = evaluate(stack.pop(), stack.pop(), stack.pop())
                stack.append(val)
        
        return stack[-1]

