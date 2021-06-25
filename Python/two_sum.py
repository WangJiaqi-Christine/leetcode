class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        while i < len(nums) - 1:
            j = i+1
            while j < len(nums):
                if nums[i] +nums[j] == target:
                    output = [i, j]
                    break
                j += 1
            i += 1
        return output
            
