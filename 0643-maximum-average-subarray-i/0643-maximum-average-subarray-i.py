class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = curr = sum(nums[:k]) #sum of first window and we assume it to be max
        
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k] #we add the number entering and remove the leaving number, by sliding the window
            ans = max( ans, curr)
        return ans/k
