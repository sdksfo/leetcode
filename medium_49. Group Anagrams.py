
# Explanation

# anagrams when sorted yields the same string e.g tea and ate when sorted gives 'aet'. Group each
# anagram using its sorted string as key.

import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = collections.defaultdict(list)
        for str_ in strs:
        	hashmap[''.join(sorted(str_))].append(str_)
        return hashmap.values()

print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
