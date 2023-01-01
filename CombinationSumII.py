def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    combinations = []
    length = len(candidates)
    seen = []
    def find_sum(combination, idx, seen):
        if(sum(combination) == target):
            if(not combination[:] in combinations):
                combinations.append(combination[:])
            for num in combination:
                seen.append(candidates.index(num))
            return
        if(sum(combination) > target):
            return
        for i in range(idx, length):
            if i in seen:
                continue
            combination.append(candidates[i])
            find_sum(combination, min(i+1, len(candidates)-1), seen)
            seen = []
            combination.pop()
    find_sum([], 0, seen)
    
    return combinations