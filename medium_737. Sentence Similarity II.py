
"""
Two sentences are similar if each word in them has the same parent.


For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar,

[["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

In the above example,

parent of great is good
parent of good is good
parent of fine is good

[["great", "good"], ["fine", "like"], ['good', 'like']].

great - good
fine - like
like - good

great, fine and like are all pointing at good
"""

class Solution(object):
    def getParent(self, child):
        if child in self.parent:
            return self.getParent(self.parent[child])
        return child

    def union(self, child, parent):
        if child != parent:
            self.parent[child] = parent

    def areSentencesSimilarTwo(self, words1, words2, pairs):
        if len(words1) != len(words2): return False
        self.parent = {}
        for word1, word2 in pairs:
            parent1 = self.getParent(word1)
            parent2 = self.getParent(word2)
            self.union(parent1, parent2)
        return all(self.getParent(i)==self.getParent(j) for i,j in zip(words1, words2))

print Solution().areSentencesSimilarTwo(["great", "acting", "skills"], ["fine", "drama", "talent"],[["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]])
