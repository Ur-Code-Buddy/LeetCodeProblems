class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        doubles = []
        uniquevalues = set(arr)
        for i in uniquevalues:

            doubles.append(arr.count(i))
        if len(doubles) == len(set(doubles)):
            return True
        return False
        