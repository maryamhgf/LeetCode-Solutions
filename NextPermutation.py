class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def swap(nums, idx1, idx2):
            nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
            return nums
        
        def find_pivot(nums):
            idx = len(nums) - 1
            while(idx >= 1):
                if(nums[idx] > nums[idx - 1]):
                    return idx - 1
                idx = idx - 1
            return idx 

        pivot = find_pivot(nums)
        print(pivot)
        swapped = 0
        for i in range(len(nums)-1, pivot, -1):
            if(nums[pivot] < nums[i]):
                nums = swap(nums, pivot, i)
                print(nums)
                swapped = 1
                break
        if(not swapped):
            nums = swap(nums, pivot, len(nums) - 1)
        temp = nums[pivot+1:]
        temp.sort()
        nums[pivot+1:] = temp
        return nums


