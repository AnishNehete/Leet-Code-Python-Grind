class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {')':'(',']':'[','}':'{'} #this will tell us which opening bracket should match each closing bracket
        for ch in s: #we go left to right

            if ch in "([{":  # if current bracket is opening bracket we caanot pop it so we store it in stack
                stack.append(ch)

            else:   #if closing bracket directly out
                if not stack: #no opening bracket available to match this
                    return False
            
                top = stack.pop() #remove the most recent opening bracket

                if top != mapping[ch]:
                    return False
        
        return len(stack) == 0


