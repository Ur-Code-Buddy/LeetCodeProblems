class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        r = len(s) - 1
        res = 0
        while (True):
            if res and s[r] == ' ':
                return res
            elif s[r] != ' ':
                res += 1
            r -= 1
            
            if r < 0:
                return res

        