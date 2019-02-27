
# Why is this a DP problem ?

# Because the rectangle ending at


[[0, 0, 1, 1, 0],
 [0, 0, 1, 1, 0],
 [0, 0, 1, 1, 0],
 [0, 0, 0, 0, 0]]

import collections

# Each level adds one to the current rectangle, ie the most bottom one and also adds an incremental factor to the count

# first rectangle, cache = 0 + (1+0) => 1, where 0 is the factor here

# second rectangle, cache = 1 + (1+1) => 3, where 1 is the factor here

# third rectangle, cache = 3 + (1+2) => 6, where 2 is the factor here

# fourth rectangle, cache = 6 + (1+3) => 10, where 3 is the factor here

# result = curr_non-cache data

class Solution:
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:return 0
        res, cache = 0, collections.defaultdict(int)
        for r in grid:
            cur=[i for i,v in enumerate(r) if v ==1]
            for each in ((a,b) for a in cur for b in cur if a<b):
                res+=cache[each]
                cache[each]+=1
        return res

print Solution().countCornerRectangles(
    [[0, 0, 1, 1, 0],
     [0, 0, 1, 1, 0],
     [0, 0, 1, 1, 0],
     [0, 0, 1, 1, 0],
     [0, 0, 1, 1, 0]])
