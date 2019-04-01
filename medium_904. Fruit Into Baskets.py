# Explanation:

# We maintain a running basket of two fruits.

# We maintain a `tuple` of counts for each tree in the DP table:

# idx[0] = increment if the fruit can be added to the basket
# idx[1] = increment if the left tree has the same fruit as current tree

# If the fruit is already in the basket:
# 	dp[i][0] = dp[i-1][0] + 1
#   dp[i][1] = dp[i-1][1] + 1 (if left fruit is same as current fruit) or 1

# if the fruit is not in the basket:
#   basket = fruit and left tree's fruit
#   dp[i][0] = dp[t-1][1] + 1 (we increment based on the left tree's fruit)
#   dp[i][1] = 1

# (e.g)
# tree   = [ 1,     1,     2,     2,     1,     2,     2,     3,      3,     3,     2,     3,     2,     4,    3,        3 ]
# dp     = [(1,1),(2,2), (3,1), (4,2), (5,1), (6,1), (7,2), (3, 1), (4,2), (5,3), (6,1), (7,1), (8,1),  (2,1), (2,1), (3,2)]
# basket = |             (1,2)                         |                   (3,2)                  |(2,4) |    (4,3)      |

# max fruits = 8

class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        dp, basket = [(1,1)] * len(tree), set((tree[0],))
        max_fruits = 1

        for t in xrange(1, len(tree)):
        	if tree[t] in basket:
        		dp[t] = (dp[t-1][0] + 1, dp[t-1][1] + 1 if tree[t] == tree[t-1] else 1)
        	else:
        		basket = set((tree[t], tree[t-1]))
        		dp[t] = (dp[t-1][1] + 1, 1)
        	max_fruits = max(max_fruits, dp[t][0])
        return max_fruits

print Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4])

class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if not tree: return 0

        curr, prev, max_len, curr_len = (tree[0], 0), None, 0, 1

        for idx, fruit in enumerate(tree[1:]):
            idx += 1
            if fruit == curr[0]:
                curr_len += 1
                curr = (fruit, idx)
            elif not prev or fruit == prev[0]:
                curr_len += 1
                curr, prev = (fruit, idx), curr
            else:
                max_len = max(max_len, curr_len)
                curr_len = idx - prev[1]
                curr, prev = (fruit, idx), curr
        return max(max_len, curr_len)
