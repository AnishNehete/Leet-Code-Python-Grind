import numpy as np
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        #While simulate, we know each row has m elements. So, instead of adding each element one-by-one, we can iterate through the original array in steps of size n, directly creating and adding subarrays that represent each row in the 2D array. This will simplify the approach by avoiding the need for nested loops.
        res = []
        for i in range (0, len(original), n): 
            res.append(original[i : i+n])
        return res