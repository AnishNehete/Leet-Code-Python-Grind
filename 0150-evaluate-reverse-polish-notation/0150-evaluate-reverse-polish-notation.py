class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in {"+" , "-" , "*", "/"}: #if token not in operator
                stack.append(int(token))
            else:
                right=stack.pop() #pop most recent number , right operand
                left = stack.pop()

                if token == "+":  # If operator is plus
                    stack.append(left + right)  # Add both numbers and push result back
                elif token == "-":  # If operator is minus
                    stack.append(left - right)  # Subtract in correct order: left minus right
                elif token == "*":  # If operator is multiply
                    stack.append(left * right)  # Multiply both numbers and push result back
                else:  # The only operator left is division "/"
                    stack.append(int(float(left) / right))  # Divide and truncate toward zero, not floor

        return stack[-1]