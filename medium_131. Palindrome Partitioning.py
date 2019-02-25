
# Input: "aab"
# Output:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

class Solution(object):

    def isPalin(self, substring):
        return substring == substring[::-1]

    def partition(self, s):
        if not s: return [[]]
        output = []
        others = self.partition(s[1:])
        for other in others:
            curr = s[0]
            output.append([curr] + other)
            for p in xrange(len(other)):
                curr += other[p]
                if curr[0] == curr[-1] and self.isPalin(curr) and [curr] + other[p+1:] not in output:
                    output.append([curr] + other[p+1:])
        return output

print Solution().partition('aaabab')
