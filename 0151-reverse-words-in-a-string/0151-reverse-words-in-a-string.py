class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        
        """

        s = s.split()
        return " ".join(s[::-1])