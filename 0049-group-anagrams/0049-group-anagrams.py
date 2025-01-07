class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashset = {}
        for word in strs:
            sorted_word = " ".join(sorted(word))
            if sorted_word in hashset:
                hashset[sorted_word].append(word)
            else:
                hashset[sorted_word] = [word]
        return hashset.values()
        