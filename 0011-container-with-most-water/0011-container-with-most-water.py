class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        volume = 0
        
        while (left < right ):
            if height[left] < height[right]:
                volume = max(height[left] * (right-left), volume)
            else:
                volume = max(height[right] * (right-left), volume)
            
                
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return volume