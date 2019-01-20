
# Explanation:

# Build the tree from bottom up. The value for n is computed by adding '()' to every result from n-1.

# (e.g)

# n = 1:
#  ['()']

# n = 2:
#  Add '()' after every char in every item in n=1 i.e insert '()' after every char in ['()']
#  The first char for n=1 is '(', so inserting '()' makes it '(())'
#  The second char for n=1 is ')', so inserting '()' makes it '()()'
#  The result is ['(())', '()()']

# n = 3:
#  Result from n=2 is ['(())', '()()']
#  Adding '()' after every char from the result set makes result as:
#  For '(())':
#  	(()())
#  	((()))
#  	(()())
#  	(())()
#  For '()()':
#   (())() -> This needs to be excluded as its already computed. So i use a `set` to eliminate duplicates.
#   ()()()
#   ()(())
#   ()()() -> duplicate
#  The result set for 3 is ['()(())', '((()))', '(()())', '(())()', '()()()']


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1: return ['()']
        result = set()
        for braces in self.generateParenthesis(n-1):
        	for idx in xrange(len(braces)):
        		result.add(braces[:idx+1]+'()'+braces[idx+1:])
        return list(result)

print Solution().generateParenthesis(3)
