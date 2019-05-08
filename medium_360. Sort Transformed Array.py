
# Approach: Checked hint: Parameter A in: A * x^2 + B * x + C dictates the shape of the parabola.
# Positive A means the parabola remains concave (high-low-high), but negative A inverts the parabola to be convex (low-high-low).

# Based on value of A, determine if the output array have to be filled from the right to left or from left to right.

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        i, j, t, output = 0, len(nums)-1, len(nums)-1 if a >= 0 else 0, [0] * len(nums)

        nums = [(lambda x: (a*(x**2)) + (b*x) + c)(x) for x in nums]

        while i <= j:
            if (a >= 0 and nums[i] > nums[j]) or (a < 0 and nums[i] < nums[j]):
                output[t] = nums[i]
                i += 1
            else:
                output[t] = nums[j]
                j -= 1
            t = t - 1 if (a >= 0) else t + 1

        return output

print Solution().sortTransformedArray([-4, -2, 0, 2, 4], 1, 3, 5)
