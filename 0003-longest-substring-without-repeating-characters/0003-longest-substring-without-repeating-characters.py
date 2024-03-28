class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        max_length = 0
        length = len(s)
        
        hashset = set()
        
        for r in range(length):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            max_length = max(max_length, r - l + 1)
        return max_length
            
        
#         while ( r < length):
#             if s[r] in hashset:
#                 pass
#             else:
#                 hashset.add(char)
                
#             r += 1
            
#             max_length = max(max_length, r - l)
        
        