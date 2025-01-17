class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]  # Initialize stack with -1 to handle base case
        max_length = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Push the index of '('
            else:
                stack.pop()  # Pop for a matching ')'
                if not stack:
                    stack.append(i)  # If stack is empty, push the current index
                else:
                    max_length = max(max_length, i - stack[-1])  # Update max length

        return max_length


