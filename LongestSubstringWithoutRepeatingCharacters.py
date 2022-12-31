class Solution(object):
    def reset_stack(self, stack, last):
        split_indx = stack.index(last)
        return stack[split_indx+1: ]

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        lengths = []
        s_list = list(s)
        if(len(set(s_list)) == 1):
            return 1
        while(s_list):
            last = s_list.pop()
            if(last in stack):
                #resetting
                lengths.append(len(stack))
                stack = self.reset_stack(stack, last)
                
            stack.append(last)
        lengths.append(len(stack))
        print(lengths)
        return max(lengths)