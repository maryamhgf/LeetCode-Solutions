class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        read_row = 0
        read_col = 0
        rows_inf = {}
        if(numRows == 1):
            return s
        for char in s:
            try:
                rows_inf[read_row] += [char]
            except:
                rows_inf[read_row] = [char]
            if(read_col % (numRows-1) == 0):
                if(read_row == numRows-1):
                    read_col += 1
                    read_row -= 1
                else:
                    read_row += 1
            else:
                read_row -= 1
                read_col += 1
                if(read_col % (numRows-1) == 0):
                    read_row = 0

        output_string = ''
        print(rows_inf)
        for v in rows_inf.values():
            for i in range(len(v)):
                output_string += v[i]
        return output_string
