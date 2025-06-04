class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r = len(numbers)-1
        while l < r:
            currsum = numbers[l]+ numbers[r]
            if currsum > target:
                r -=1
            if currsum < target:
                l +=1
            if currsum == target:
                return [l+1, r+1]
                