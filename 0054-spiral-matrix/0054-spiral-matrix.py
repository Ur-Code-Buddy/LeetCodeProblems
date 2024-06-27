class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        rows = len(matrix)  #n
        col = len(matrix[0]) #m

        top = 0
        left = 0
        bottom = rows - 1
        right = col - 1

        while (top <= bottom and left <= right):

            #for moving left to right
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1 
            #for moving top to down
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1
            #for right to left
            if (top <= bottom): 
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -=1 
            #for bottom to up
            if ( left <= right):
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
        return ans



