class Solution(object):
    def mergeAlternately(self, word1, word2):
        i = j = 0
        ms = []
        while i < len(word1) and j < len(word2):
            ms.append(word1[i])
            ms.append(word2[j])
            i += 1
            j += 1

        while j < len(word2):
            ms.append(word2[j])
            j += 1

        while i < len(word1):
            ms.append(word1[i])
            i+= 1
        
        return "".join(ms)