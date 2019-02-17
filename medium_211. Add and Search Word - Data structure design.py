

class TrieNode(object):
	def __init__(self, val):
		self.val = val
		self.children = {}
		self.count = 0


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('root')

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for char in word:
        	if char not in node.children:
        		new_node = TrieNode(char)
        		node.children[char] = new_node
        	node = node.children[char]
        node.count += 1

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def get_item(w, node):
        	for c in xrange(len(w)):
        		if w[c] == '.':
        			return any([get_item(w[c+1:], v) for k,v in node.children.items()])
        		elif w[c] in node.children:
        			node = node.children[w[c]]
        		else:
        			return False
        	return node.count != 0
        return get_item(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("baed")
print obj.search("b..d")
