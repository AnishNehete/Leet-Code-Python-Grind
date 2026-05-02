import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} #store freq
        
        for num in nums: #count each num
            freq[num] = 1 +freq.get(num,0) #if number already exists then we can start with 1 or start with 0

        heap = [] #each entry will be count

        for num, count in freq.items():
            heapq.heappush(heap, (count,num))

            if len(heap) > k:
                heapq.heappop(heap)

        result =[]

        while heap:
            count, num = heapq.heappop(heap)
            result.append(num)

        return result

        