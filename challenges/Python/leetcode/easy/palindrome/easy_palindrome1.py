class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str1 = str(x)
        n = len(str1)
        for i, el in enumerate(str1):
            n -= 1
            if (el != str1[n]):
                return False
        return True

