
class Node(object):
	def __init__(self, val):
		self.val = val
		self.children = {}
		self.count = 0


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('root')

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for char in word:
        	if char in node.children:
        		node = node.children[char]
        	else:
        		char_node = Node(char)
        		node.children[char] = char_node
        		node = node.children[char]
        node.count += 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
        	if char in node.children:
        		node = node.children[char]
        	else:
        		return False
        return node.count != 0


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
        	if char in node.children:
        		node = node.children[char]
        	else:
        		return False
        return True

t = Trie()
t.insert('Apple')
print t.startsWith('Apple')
t.insert('Ape')
print t.search('Ape')
