class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l=0
        arr=[]
        for r in range(1,len(nums)):
            if nums[r] != nums[l]:
                l+=1
                nums[l] = nums[r]
            
        return l+1