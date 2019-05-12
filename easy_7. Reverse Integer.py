class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        output, sign, x = 0, x > 0, abs(x)

        while x:
        	output = (output*10) + (x%10)
        	x = x/10

        output = output if sign else -output
        
        if (output < (-2 ** 31)) or (output > (2 ** 31)-1):
            return 0
        
        return output    
 