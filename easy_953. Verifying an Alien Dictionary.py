
# Custom Sort Order
# Given a list of strings and a list of characters that specifies a custom sort ordering, return true if the strings are sorted in the correct order otherwise return false
# Example:
# Strings: ["cb", "ca", "bc", "ba"] Order: ['c', 'b', 'a'] -> True
# Strings: ["cb", "ca", "ca","bc", "ba"] Order: ['c', 'b', 'a'] -> True
# Strings: ["bc", "ab", "ac", "ca"] Order: ['c', 'b', 'a'] -> False
# Strings ["catt", "cat", "bat"] Order ['c', 'b', 'a', 't'] -> False

# ['aarvark', "and", "cat"] [a, n, r]

# Observations:

# ["cb", "ca", "ca", "bc", "ba"] Order: ['c', 'b', 'a']

# 1) First characters match, then what is the order inside the string.
# 2) First characters do not match, then its based on the order seen

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        hashmap = {char:idx for idx, char in enumerate(order)}

        def compare(a, b):
            i = 0

            if b[i] != a[i]:
                return hashmap[b[i]] > hashmap[a[i]]

            while i < len(a) and i < len(b):
                if hashmap[a[i]] > hashmap[b[i]]:
                    return False
                i += 1

            return len(a) <= len(b)

        for i in xrange(len(words)-1):
            if not compare(words[i], words[i+1]):
                return False

        return True

print Solution().isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")
