class Solution(object):
    def twoSum(self, nums, target):
        HashTable = [[] for _ in range(10)]
        def Hashing(keyvalue):
            return keyvalue % len(HashTable)
        def insert(Hashtable, keyvalue, value): 
            hash_key = Hashing(keyvalue)
            Hashtable[hash_key].append(value)
        def check_sums(nums, number, target):
            for value in values:
                if nums[value] + number == target:
                    return value
            return -1
        results = []
        for i in range(len(nums)):
            values = HashTable[Hashing(nums[i])]
            if(values != []):
                value = check_sums(nums, nums[i], target)
                if(value != -1):
                    results.append(value)
                    results.append(i)
                    return results
                    break
                #return results
            insert(HashTable, target - nums[i], i)