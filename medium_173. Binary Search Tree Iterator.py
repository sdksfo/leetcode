
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# nodes = [TreeNode(i) for i in (1,2,3,4,5,6,7,8,9)]

def create_bst(array):
	if array:
		mid = len(array)/2
		root = TreeNode(array[mid])
		root.left = create_bst(array[:mid])
		root.right = create_bst(array[mid+1:])
		return root

root = create_bst([1,2,3,4,5,6,7,8,9])


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack, node, self.next_node = [], root, None
        while node:
        	self.stack.append(node)
        	node = node.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        node = self.stack.pop()
        self.next_node = node.right
        return node.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        while self.next_node:
        	self.stack.append(self.next_node)
        	self.next_node = self.next_node.left
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
obj = BSTIterator(root)
print obj.next()
print obj.hasNext()
print obj.next()
print obj.hasNext()
print obj.next()
print obj.hasNext()
print obj.next()
print obj.hasNext()
print obj.next()
print obj.hasNext()
print obj.next()
print obj.hasNext()
print obj.next()
print obj.hasNext()
print obj.next()
print obj.hasNext()
print obj.next()
print obj.hasNext()
