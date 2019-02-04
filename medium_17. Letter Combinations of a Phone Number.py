
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


class Solution(object):
    chars = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits:
            if digits in self.chars:
                return list(self.chars[digits])
            return [char+i for char in self.chars[digits[0]] for i in self.letterCombinations(digits[1:])]
        return []

