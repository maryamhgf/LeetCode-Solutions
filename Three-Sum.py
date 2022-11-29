def twoSum(nums, target):
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
                results.append([nums[value], nums[i]])
        insert(HashTable, target - nums[i], i)
    return results

def threeSum(nums):
    results = []
    for i in range(len(nums)):
        result_two_sums = twoSum(nums[i+1:], -1 * nums[i])
        for result in result_two_sums:
            results.append([result[0], result[1], nums[i]])
    print(results)