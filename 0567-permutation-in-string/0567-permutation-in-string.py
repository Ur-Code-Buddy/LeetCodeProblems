# class Solution(object):
#     def checkInclusion(self, s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: bool
#         """
#         if len(s1) > len(s2):
#             return False
        
#         charmap = {}
#         for val in s1:
#             if val in charmap:
#                 charmap[val] += 1
#             else:
#                 charmap[val] = 1
         
        
#         length = len(s1)
#         length2 = len(s2)
#         start = 0
#         windowed_charmap = {}
#         for r in range(start, length2):
#             if s2[r] in windowed_charmap:
#                 windowed_charmap += 1
#             else:
#                 windowed_charmap = 1
            
            
#             if windowed_charmap == charmap:
#                 return True
#             else:
#                 start += 1
#                 windowed_charmap[r] -= 1
#                 if windowed_charmap[r] == 0:
#                     del windowed_charmap[r]
            
class Solution(object):
    def checkInclusion(self, s1, s2):
        
        
        
        if len(s1) > len(s2):
            return False
        
        charmap = {}
        for val in s1:
            if val in charmap:
                charmap[val] += 1
            else:
                charmap[val] = 1
         
        length = len(s1)
        length2 = len(s2)
        start = 0
        windowed_charmap = {}
        for r in range(length2):
            # Expand window
            if s2[r] in windowed_charmap:
                windowed_charmap[s2[r]] += 1
            else:
                windowed_charmap[s2[r]] = 1
            
            # Check if window matches s1
            if r >= length:
                # Shrink window
                if windowed_charmap[s2[start]] == 1:
                    del windowed_charmap[s2[start]]
                else:
                    windowed_charmap[s2[start]] -= 1
                start += 1
            
            if windowed_charmap == charmap:
                return True
        
        return False

            
            
        
        
                    
                    
            
            