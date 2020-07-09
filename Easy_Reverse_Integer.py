class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = False
        if x == 0:
            return 0
        elif x < 0:
            x = -x
            flag = True
        rev = 0
        
        while x != 0:
            temp = x % 10
            x = x//10
            
            if ( rev * 10 >= 2147483648 ):
                return 0
            rev = (rev * 10) + temp
        if flag:
            rev = -rev
        return rev
