class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        current_value=0
        result = 0

        for val in range(len(gain)):
            current_value = current_value + gain[val]
            result= max(current_value,result)
        return result  
            