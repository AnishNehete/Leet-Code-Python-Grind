class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
        
        for n in numsSet:
            # checking start of the sequency
            if (n-1) not in numsSet:
                length = 0
                while (n + length) in numsSet:
                    length +=1
                #longest will keep updating in loop
                longest = max(length ,longest)
        return longest