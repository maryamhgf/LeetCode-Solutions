class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        def find_last_word_indx(s):
            indx = len(s) - 1
            while(s[indx] == " "):
                indx = indx - 1
            return indx
        indx = find_last_word_indx(s)
        current_letter = s[indx]
        indx = indx - 1
        len_last = 1
        while current_letter != " " and indx >= 0:
            current_letter = s[indx]
            len_last = len_last + 1
            indx = indx - 1
        if(current_letter == " "):
            len_last = len_last - 1
        return len_last