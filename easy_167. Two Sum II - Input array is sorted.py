

class Solution(object):
    def twoSum(self, numbers, target):
        i, j = 0, len(numbers)-1

        while i < j:
            if numbers[i] + numbers[j] == target:
                return i+1, j+1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1

print Solution().twoSum([5,25,75], 100)
