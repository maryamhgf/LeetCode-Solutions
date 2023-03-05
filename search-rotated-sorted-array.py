class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pivot = nums.index(max(nums))
        if(target == nums[pivot]):
            return pivot
        if(target <= nums[pivot] and target >= nums[0]):
            search_nums = nums[:pivot]
            index = 0
        else:
            search_nums = nums[pivot:]
            index = pivot
        for num in search_nums:
            if(target == num):
                return index
            index =  index + 1
        return -1