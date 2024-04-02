class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap = {}
        length = len(s)
        
        if length != len(t):
            return False
        
        for i in range(length):
            if s[i] in hashmap:
                if hashmap[s[i]] != t[i]:
                    return False
            else:
                if t[i] in hashmap.values():
                    return False
                hashmap[s[i]] = t[i]
        
        return True
