
# Input: "word"
# Output:
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

# For each char its 'w' + rest of the word, '1' + rest of the word

class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        if not word: return [""]

        others, output = self.generateAbbreviations(word[1:]), []

        for other in others:
            i = 0
            while i < len(other) and other[i].isdigit():
                i += 1
            nums = int(other[:i]) + 1 if other[:i] else 1
            output.append(word[0] + other)
            output.append(str(nums) + other[i:])

        return output

print Solution().generateAbbreviations('word')
