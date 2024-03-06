class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string= ""
        for letters in s:
            if letters.isalnum():
                string += letters.lower()
        return string == string[::-1]
