class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums, curr, arr_len = sorted(nums), float('inf'), len(nums)-1

        for idx in xrange(len(nums)):
            i, j, expected = idx+1, arr_len, target - nums[idx]
            while i < j:
                delta = (nums[i] + nums[j] + nums[idx]) - target
                if abs(delta) < abs(curr - target):
                    curr = nums[i] + nums[j] + nums[idx]
                if nums[i] + nums[j] > expected:
                    j -= 1
                else:
                    i += 1
        return curr
