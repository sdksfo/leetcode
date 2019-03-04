
"""

[

[0,1,1,0],
[0,1,1,0],
[0,0,0,1]

]

"""

# for each cell, lets mark the longest distance, ie from vertical, horizontal, diagonal and anti-diagonal

class Solution(object):
    def longestLine(self, M):
        rows, cols, temp, max_num, dp = len(M), len(M[0]) if M else 0, [], 0, []

        for row in xrange(rows):
            for col in xrange(cols):
                [v, h, d, a] = [M[row][col]] * 4
                if M[row][col]:
                    if row > 0:
                        v = dp[col][0] + 1
                    if col > 0:
                        h = temp[-1][1] + 1
                    if row > 0 and col > 0:
                        d = dp[col-1][2] + 1
                    if row > 0 and col < cols-1:
                        a = dp[col+1][3] + 1
                max_num = max(max([v,h,d,a]), max_num)
                temp.append([v,h,d,a])
            dp = temp
            temp = []
        return max_num

print Solution().longestLine([
    [1,1,1],
    [1,1,1],
])
