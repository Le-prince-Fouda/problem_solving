class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        character = {}
        length = 0
        subStart = 0  # index start of the substring
        for index, current in enumerate(s):
            if current in character and character[current] >= subStart:
                subStart = character[current] + 1
            character[current] = index
            length = max(length, index - subStart + 1)
        return length

