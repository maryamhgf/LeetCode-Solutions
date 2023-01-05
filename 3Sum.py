class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if(len(nums) < 3):
            return []
        nums.sort()
        result = []
        if(nums[0] > 0 or nums[-1] < 0):
            return []
        for i in range(len(nums)):
            if( i > 0 and nums[i] == nums[i-1]):
                continue
            target = 0 - nums[i]
            l = i + 1
            r = len(nums) - 1
            while(l < r):
                if(nums[l] + nums[r] < target):
                    l = l + 1
                if(nums[l] + nums[r] > target):
                    r = r - 1
                if(nums[l] + nums[r] == target and l != r):
                    result.append([nums[i], nums[l], nums[r]])
                    l = l + 1
                    r = r - 1
            
        return result