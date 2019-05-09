

class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        prev, i = '', 0

        for j in xrange(len(typed)):
        	if i < len(name) and name[i] == typed[j]:
        		prev = typed[j]
        		i += 1
        	elif typed[j] != prev:
        		return False

        return i == len(name)

print Solution().isLongPressedName("vtkgn", "vttkgnn")
