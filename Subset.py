def dfs(nums, path, res):
    res.append(path)
    for i in range(len(nums)):
        dfs(nums[i+1:], path+[nums[i]], res)
def subset(nums):
    res = []
    dfs(nums, [], res)
    return res