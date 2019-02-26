
class Solution(object):
    def combo(self, candidates, target, candy):
        if target >= 0:
            if target == 0:
                self.candies.append(candy)
            prev = None
            for c in range(len(candidates)):
                if (prev is not None and candidates[c] == prev) or candidates[c] > target:
                    continue
                candy.append(candidates[c])
                self.combo(candidates[c+1:], target-candidates[c], candy[:])
                candy.pop()
                prev = candidates[c]
            return self.candies

    def combinationSum2(self, candidates, target):
        self.candies, candidates = [], sorted(candidates)
        return self.combo(candidates, target, [])
