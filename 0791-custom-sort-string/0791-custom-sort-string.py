class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        freq = {}
        for letter in s:
            freq[letter] = freq.get(letter, 0) + 1

        result = ""
        for letter in order:
            if letter in freq:
                result += letter * freq[letter]
                freq.pop(letter)

        for letter, count in freq.items():
            result += letter * count


        return result
        