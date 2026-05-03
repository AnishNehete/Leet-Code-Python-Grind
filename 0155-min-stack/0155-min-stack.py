class MinStack:

    def __init__(self):
        self.stack = [] #main stack to store all the values
        self.min_stack = [] #min stack to store minimum values

    def push(self, val: int) -> None: 
        self.stack.append(val) #first always add new value to the main

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            current_min = self.min_stack[-1]
            self.min_stack.append(min(val,current_min))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] #last element of the main stack

    def getMin(self) -> int: #return minimum element in constant time
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()