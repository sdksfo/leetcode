
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        output, substr = [], s[:len(p)]

        hashp, hashmap = {i: p.count(i) for i in p}, {i: substr.count(i) for i in substr}

        if hashmap == hashp: output.append(0)

        for i in xrange(1, len(s)-len(p)+1):
            new_char = s[i+len(p)-1]
            prev_char = s[i-1]
            if new_char != prev_char:
                if new_char in hashmap:
                    hashmap[new_char] += 1
                else:
                    hashmap[new_char] = 1
                hashmap[prev_char] -= 1
                if hashmap[prev_char] == 0:
                    del hashmap[prev_char]
            if hashmap == hashp: output.append(i)

        return output

print Solution().findAnagrams(s, p)
