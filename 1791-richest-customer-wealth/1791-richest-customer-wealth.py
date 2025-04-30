class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum1 = 0
        a = 0
        max1 = 0
        count = 0
        
        for i in accounts:
            a = sum(i)     # sum of current customer's wealth
            sum1 = a       # store in sum1 (not +=, since we only want current customer)
            if sum1 > max1:
                max1 = sum1
        
        return max1