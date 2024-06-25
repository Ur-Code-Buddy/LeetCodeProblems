class Solution(object):

    def binary_search_exists(self,arr, target):
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
    
        return False  # Target not found

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        col = len(matrix)
        rows = len(matrix[0])

        incol = -1
        for i in range(col):
            if matrix[i][0] > target:
                incol = i - 1
                break
        res = self.binary_search_exists(matrix[incol],target)
        return res
        