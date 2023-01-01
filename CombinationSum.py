class Solution(object):
    import copy
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combinations = []
        length = len(candidates)
        def find_sum(combination, idx):
            if(sum(combination) == target):
                combinations.append(copy.deepcopy(combination))
                return
            if(sum(combination) > target):
                return
            for i in range(idx, length):
                combination.append(candidates[i])
                find_sum(combination, i)
                combination.pop()
        find_sum([], 0)
        return combinations