class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result =[] #store result 
        nums.sort() #sort the array first

        n = len(nums) #store the length of the arr

        for i in range(n-2): #we will loop because we need atleast 3 numbers to form a triplet
            if i > 0 and nums[i] == nums[i-1]: 
                continue #move the next i value
            
            left = i+1
            right = n-1

            while left <right :
                total = nums[i] + nums[left] + nums[right]

                if total ==0:
                    result.append([nums[i], nums[left], nums[right]]) #append if all match

                    left += 1 #move left first
                    right -=1 #move right first

                    while left < right and nums[left] == nums[left-1]: #skip duplicates
                        left +=1 #keep moving left until new value 

                    while left < right and nums[right] == nums[right+1]: #skip duplicates
                        right -=1 #keep moving right until new value 

                elif total < 0:
                    left +=1
                
                else:
                    right -=1

        return result #return all unique triplets 