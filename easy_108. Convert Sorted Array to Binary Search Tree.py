

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
	        num_len = len(nums)/2
	        root = TreeNode(nums[num_len])
	        root.left, root.right = self.sortedArrayToBST(nums[:num_len]), self.sortedArrayToBST(nums[num_len+1:])
	        return root

root = Solution().sortedArrayToBST([1,2,3,4,5,6,9,20,182,2810])
