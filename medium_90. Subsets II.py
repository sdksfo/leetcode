
[1, 1, 2, 2]

# 2

# 2,2

# 1,2,2

# 1,2

# 1,1,2,2

# 1,1,2


class Solution(object):
    def subsetsWithDup(self, a):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def get(a):
        	if a:
        		prev = get(a[1:])
        		return prev + [[a[0]] + i for i in prev]
        	return [[]]
        output = sorted(get(sorted(a)))
        return [d for i, d in enumerate(output) if d != output[i-1]] or [[]]


print Solution().subsetsWithDup([4,4,4,1,4])
