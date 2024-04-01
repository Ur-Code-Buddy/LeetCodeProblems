class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        end = len(s) - 1
        
        while end >= 0 and s[end] == ' ':
            end -= 1
        
        length = 0
        while end >= 0 and s[end] != ' ':
            length += 1
            end -= 1
            
        return length
        
