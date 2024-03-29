class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        hashcount = {}
        res = 0
        l = 0
        length = len(s)
        for r in range(length):
            hashcount[s[r]] = 1 + hashcount.get(s[r], 0)
            while(r-l + 1 - max(hashcount.values() ) > k ):
                hashcount[s[l]] -= 1
                l += 1
            
            res = max(r - l + 1, res)   
            
        return res
        