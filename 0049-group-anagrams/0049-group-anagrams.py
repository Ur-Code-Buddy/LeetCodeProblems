class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        
        if not strs:
            return 
        
        for val in strs:
            sorted_value = "".join(sorted(val))
            if sorted_value in hashmap:
                hashmap[sorted_value].append(val)
            else:
                hashmap[sorted_value] = [val]
                
                
        return list(hashmap.values() )
        