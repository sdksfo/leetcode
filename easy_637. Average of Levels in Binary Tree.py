
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        queue, output = [[root]], []

        while queue:
            nodes = queue.pop(0)
            if nodes:
                output.append(float(sum(node.val for node in nodes))/len(nodes))
                queue.append(filter(lambda x: x, [n.left for n in nodes]+[n.right for n in nodes]))

        return output
