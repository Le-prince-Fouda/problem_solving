class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, element in enumerate(nums):
            val = target - element
            if val in nums[i+1:]:
                j = nums.index(val, i+1)
                return [i,j]
        