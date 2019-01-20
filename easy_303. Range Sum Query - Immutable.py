# Explanation:

# sum i,j = sum until j - sum_until i-1

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = [0]*(len(nums)+1)
        for i in xrange(len(nums)):
        	self.dp[i+1] = self.dp[i]+nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j+1] - self.dp[i]


# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
print obj.sumRange(0,5)