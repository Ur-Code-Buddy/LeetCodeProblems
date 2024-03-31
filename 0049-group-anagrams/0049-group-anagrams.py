class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}

        
        for n in strs:
            sorted_word = ''.join(sorted(n))
            if sorted_word in hashmap:
                hashmap[sorted_word].append(n)
            else:
                hashmap[sorted_word] = [n]
        return list(hashmap.values() )
                
        