
# Explanation
# Do a BFS traversal of the words by changing each char of the word at a time

# Notes:
# Maintain a set() to capture all words seen before
# If the transformed word is already `seen` ie the path is already taken we ignore
# Since its a BFS, we separate each level with a empty string ''. The number of '' encountered indicates the
# depth of the tree or the transformations required to change from beginword -> endword

class Solution(object):
    def ladderLength(self, begin, end, word_list):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        allwords, chars, words, seen, count = set(word_list), [{word[i] for word in word_list} for i in xrange(len(begin))], [begin, ''], set(), 1
        while words:
            word = words.pop(0)
            if word == end: return count
            if word:
                new_words = [w for w in [word[:i]+c+word[i+1:] for i, char in enumerate(chars) for c in char] if w not in seen and w in allwords]
                seen.update(new_words)
                words.extend(new_words)
            else:
                count += 1
                words.append('') if words else ''
        return 0

print Solution().ladderLength('nanny', 'aloud', ["ricky","grind"])
