

"""

[1, 1, 1, 1, 1], S is 3

output = 5

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

"""

# class Solution(object):
#     cache = {}
#     def findTargetSumWays(self, nums, S):
#         """
#         :type nums: List[int]
#         :type S: int
#         :rtype: int
#         """
#         if not S and not nums:
#             return 1
#         total = sum(nums)
#         if nums:
#             if (S, total) not in self.cache:
#                 self.cache[(S, total)] = self.findTargetSumWays(nums[1:], S+nums[0]) + self.findTargetSumWays(nums[1:], S-nums[0])
#             return self.cache[(S, total)]
#         return 0


# print Solution().findTargetSumWays([2,20,24,38,44,21,45,48,30,48,14,9,21,10,46,46,12,48,12,38], 48)

class Solution(object):
    cache = {}
    def findTargetSumWays(self, nums, S, I=0):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if I == len(nums):
            return not S
        if (S, I) not in self.cache:
            self.cache[(S, I)] = self.findTargetSumWays(nums, S+nums[I], I+1) + self.findTargetSumWays(nums, S-nums[I], I+1)
        return self.cache.get((S, I), 0)

# class Solution(object):
#     def dfs(self, nums, S, I):
#         if not S and not nums:
#             return 1
#         if nums and (S, I) not in self.cache:
#                 self.cache[(S, I)] = self.dfs(nums[1:], S+nums[0], I+1) + self.dfs(nums[1:], S-nums[0], I+1)
#         return self.cache.get((S, I), 0)

#     def findTargetSumWays(self, nums, S, I=0):
#         """
#         :type nums: List[int]
#         :type S: int
#         :rtype: int
#         """
#         self.cache = {}
#         return self.dfs(nums, S, 0)

print Solution().findTargetSumWays([0,0,0], 0)
