def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    result = '1'
    def say(string):
        num_repetition = 1
        num = string[0]
        output = ''
        for i in range(1, len(string)):
            if(string[i] != num):
                output += str(num_repetition)
                output += num
                num = string[i]
                num_repetition = 1
            else:
                num_repetition += 1
        return output+str(num_repetition)+num
    for i in range(1, n):
        result = say(result)
    return result
print(countAndSay(1))
