"""
Requirement:
a) Given a string and a list of words, return how many words in the list can be stretched to form the input string

Examples:
heeelo -> helo
heeeloo != helo
heeelo != hi
heelooo -> heelo
heeeelooo -> heelo

Understanding: (After pre-processing we create a list of tuples)
a) If len of chars at A is more than or equal to B and char count at A is atleast 3 -> stretchy
b) If len of chars at A is more than B and char count at A is less than 3 -> not stretchy (we can discard)
c) If char at A is not equal to B -> not stretchy (we can discard)
d) If len of A array is different from len of B array -> not stretchy (we can discard)

Approach:
a) We can pre-process and store in array
b) Apply rules above to determine stretchy or not
"""


class Solution(object):
    def get_rle(self, string):
        groups = []
        for char in string:
            if not groups or groups[-1][0] != char:
                groups.append([char, 0])
            groups[-1][1] += 1
        return groups

    def is_expressive(self, s, w):
        if len(s) != len(s):
            return False
        for (s_char, s_count), (w_char, w_count) in zip(s, w):
            if s_char != w_char or w_count > s_count or (s_count < 3 and s_count != w_count):
                return False
        return True

    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        string_rle, expressive = self.get_rle(S), 0

        for word in words:
            word_rle = self.get_rle(word)
            expressive += self.is_expressive(string_rle, word_rle)

        return expressive

print Solution().expressiveWords('heeelloo', ["hello"])
