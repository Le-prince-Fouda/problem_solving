class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str1 = str(x)
        n = len(str1)
        for i in range(n // 2):
            n -= 1
            if (str1[i] != str1[n]):
                return False
        return True