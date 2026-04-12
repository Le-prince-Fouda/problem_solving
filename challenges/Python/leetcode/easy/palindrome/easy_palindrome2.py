class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str1 = str(x)
        str2 = str1[::-1] # str2 is the inverse of str1
        if (str1 == str2):
            return True
        else:
            return False

