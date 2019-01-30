
# Explanation

# Use a hashmap to store the index of the chars seen thus far. Update the start_pos
# and end_pos of your unique sequence based on whether the chars have been seen thus far or not
# and if the char index is part of your sequence

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap, start_pos, max_length = {}, 0, 0

        for idx, char in enumerate(s):
        	start_pos = hashmap[char] + 1 if hashmap.get(char, -1) >= start_pos else start_pos
        	max_length = max(idx - start_pos + 1, max_length)
        	hashmap[char] = idx

        return max_length

print Solution().lengthOfLongestSubstring("abccccccccdef")
