class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxprod = 0 #outside loop so that it tracks global max
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # avoid repeating pairs and self-product
                current = (nums[i] - 1) * (nums[j] - 1)
                if current > maxprod:
                    maxprod = current
        return maxprod