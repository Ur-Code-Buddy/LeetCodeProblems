class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        number1 = number2 = float("inf")

        for elements in nums:
            if elements <= number1:
                number1 = elements
            elif elements <= number2:
                number2 = elements
            else: return True
        return False