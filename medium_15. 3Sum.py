class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)

        prev, output = None, set()

        for idx, num in enumerate(nums):
            if nums[idx] == prev: continue

            i, j, exp = idx+1, len(nums)-1, 0-nums[idx]

            while i < j:
                total = nums[i] + nums[j]
                if total == exp:
                    output.add((nums[idx], nums[i], nums[j]))
                    i += 1
                    j -= 1
                elif total < exp:
                    i += 1
                else:
                    j -= 1

            prev = nums[idx]

        return [list(i) for i in output]
