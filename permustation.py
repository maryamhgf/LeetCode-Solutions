class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, path, res):
            if (len(nums) == 0):
                res.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
        
        res = []
        dfs(nums, [], res)
        return res