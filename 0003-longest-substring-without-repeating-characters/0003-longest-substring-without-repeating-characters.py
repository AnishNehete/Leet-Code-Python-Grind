class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 #left point of our sliding window
    
        max_length = 0 #max length so far
        last_seen ={} #dict to store most recent Index

        for right in range(len(s)): #right pointer moves 
            char = s[right]

            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1
            
            last_seen[char] = right
            
            current_length = right - left + 1

            max_length = max(max_length, current_length)
        
        return max_length