class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(nums, path, res, k):
            if(len(path) == k):
                res.append(path)
            if(len(path)>k):
                return
            for i in range(len(nums)):
                dfs(nums[i+1: ], path + [nums[i]], res, k)
        nums = list(range(1, n+1))
        res = []
        dfs(nums, [], res, k)
        return res