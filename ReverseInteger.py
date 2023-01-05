class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        output = ""
        x_int = abs(int(x))
        print("x_int: ", x_int)
        while(x_int != 0):
            new_int = x_int % 10
            x_int = x_int // 10
            output = output + str(new_int)
        if(int(x) < 0):
            output = "-" + output
        return int(output)