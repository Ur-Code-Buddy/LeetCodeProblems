class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        
        length = len(height)
        left_max = [0] * length
        right_max = [0] * length
        water_trapped = 0
        
        left_max[0] = height[0]
        for i in range(1, length):
            left_max[i] = max(left_max[i - 1], height[i])
        
        right_max[length - 1] = height[length - 1]
        for i in range(length - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
        for i in range(length):
            water_trapped += min(left_max[i], right_max[i]) - height[i]
        
        return water_trapped
