class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        """
        not optimal solution
        arr=[]
        l= 0

        r = len(nums)-1
        for i in range(k):
            for i in nums:
                while l < r:
                    a =nums[-1]
                    nums.pop(-1)
                    nums.insert(0,a)
                    """
        
        r= len(nums)-1
        k = k% len(nums)
        def reverse(l,r):
            while l < r:
                nums[l],nums[r] = nums[r], nums[l]
                l += 1 
                r -= 1
        # reverse nums
        reverse(0, len(nums) - 1)
        
        # reverse nums[:k]
        reverse(0, k - 1)
        
        # reverse nums[K:]
        reverse(k, len(nums) - 1)

