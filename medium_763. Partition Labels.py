"""
Create a map of the characters and their last position in the string. Do the below

a) Start from the first character and check the last index of the element (which indicates the end of a partition)
b) For every character read that is within the last_index computed above, check if the read character's last index is greater than prev last index. If so
   make this the new partition boundary.
c) If not, make this the beginning of a new partition
"""

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        hashmap = {s:i for i,s in enumerate(S)}

        curr_start, curr_end, output = 0, 0, []

        for idx, char in enumerate(S):
        	if idx <= curr_end:
        		curr_end = max(hashmap[char], curr_end)
        	else:
        		output.append(curr_end-curr_start+1)
        		curr_start, curr_end = idx, hashmap[char]

        output.append(curr_end-curr_start+1)

        return output

print Solution().partitionLabels("abcdefghijklmnopqrstuvwxyzzy")
