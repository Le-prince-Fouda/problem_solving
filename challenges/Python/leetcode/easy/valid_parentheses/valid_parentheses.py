class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        end = [')', '}', ']']
        start = ['(', '{', '[']
        string = []
        result = 0
        for el in s:
            if el in start:
                if el == start[0]:
                    string.append(end[0])
                elif el == start[1]:
                    string.append(end[1])
                elif el == start[2]:
                    string.append(end[2])
            if el in end:
                if len(string) != 0:
                    if string[-1] == el:
                        string.pop()
                    else:
                        return False
                else:
                    return False
        if len(string) == 0:
            return True
        else:
            return False

