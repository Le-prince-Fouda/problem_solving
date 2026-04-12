class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        n = len(s) - 1
        num = 0
        for i, el in enumerate(s):
            if i < n and roman[el] < roman[s[i + 1]]:
                num -= roman[el]
            else:
                num += roman[el]
        return num
