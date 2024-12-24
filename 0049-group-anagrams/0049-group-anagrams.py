class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashset = {}
        for i in strs:
            sorted_var = "".join(sorted(i))
            if sorted_var in hashset:
                hashset[sorted_var].append(i) 
            else:
                hashset[sorted_var] = [i]
        return list(hashset.values() )