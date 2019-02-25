
# Input: "aab"
# Output:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

class Solution(object):
    hashmap = {'':[[]]}

    def isPalin(self, substring):
        return substring == substring[::-1]

    def partition(self, s):
        if s in self.hashmap: return self.hashmap[s]
        output = []
        for i in range(1, len(s)+1):
            if self.isPalin(s[:i]):
                output.extend([s[:i]] + j for j in self.partition(s[i:]))
        self.hashmap[s] = output
        return output

print Solution().partition('aaabab')
