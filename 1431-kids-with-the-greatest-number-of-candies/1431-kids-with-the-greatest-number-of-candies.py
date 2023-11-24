class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        temp = []
        for i in range( len(candies) ):
            temp.append(candies[i] )
        temp.sort()
        largest_element = temp[len(candies) - 1]
        
        for i in range(len(candies)):
            if (candies[i] + extraCandies >= largest_element):
                result.append(True)
            else: result.append(False)
            
        return result