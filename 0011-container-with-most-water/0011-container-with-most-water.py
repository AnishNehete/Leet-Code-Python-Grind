class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            current_height = min(height[left],height[right]) #we need to use smaller height , as height of water is limited by the smaller line
            width = right - left
            area = current_height * width

            max_area = max(max_area , area)

            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        
        return max_area