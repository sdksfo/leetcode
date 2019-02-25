
class Solution(object):
    def combo(self, candidates, target, candy):
        if target >= 0:
            if target == 0:
                self.candies.append(sorted(candy))
            for c in range(len(candidates)):
                candy.append(candidates[c])
                self.combo(candidates, target-candidates[c], candy[:])
                candy.pop()
            return self.candies

    def combinationSum(self, candidates, target):
        self.candies = []
        combos = set(tuple(x) for x in self.combo(candidates, target, []))
        return [list(a) for a in combos]

print Solution().combinationSum([2,3,5], 8)
