class Solution(object):

    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lengthS = len(s)
        lengthT = len(t)
        if lengthS > lengthT: return False
        if lengthS == 0: return True

        i = 0
        for j in range(0,lengthT ):
            if i <= lengthS - 1:
                if s[i] == t[j]:
                    i = i + 1
        return i == lengthS

