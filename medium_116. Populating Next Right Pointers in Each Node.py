
"""
Do a BFS of the tree and make the next pointer of prev_node as current node.
The value `None` in the queue separates two different levels.
"""

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
    	queue, prev_node = [root, None] if root else [], None

    	while queue:
    		root = queue.pop(0)
    		if root:
    			queue.extend(filter(lambda x: x, (root.left, root.right)))
    			if prev_node:
    				prev_node.next = root
    			prev_node = root
    		else:
    			queue.append(None) if queue else None
    			prev_node = None


print Solution().connect(n[1])
