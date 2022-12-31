class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = [nums[0]]
        for num in nums[1:]:
            sums.append(max(sums[-1] + num, num))
        return max(sums)