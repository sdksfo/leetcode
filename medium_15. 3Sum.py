

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums, output = sorted(nums), set()

        for idx in xrange(len(nums)-1):
            if idx > 0 and nums[idx] == nums[idx-1]: continue
            i, j, expected = idx+1, len(nums)-1, 0-nums[idx]
            while i < j:
                if nums[i] + nums[j] == expected:
                    output.add((nums[idx], nums[i], nums[j]))
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] < expected:
                    i += 1
                else:
                    j -= 1
            prev = nums[idx]
        return list(list(i) for i in output)

print Solution().threeSum([-2,0,0,2,2])
