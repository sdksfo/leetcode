# Explanation:

# The problem can be simplified as filling every alternative hole in the array with the next biggest number

# Solution

# Create an empty array and fill with holes
# Read the sorted input array
# Fill the output array with alternative holes until all input elements are exhausted

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck, deck_len, i, hole_found = sorted(deck), len(deck), 0, True
        output = [None] * len(deck)

        for card in deck:
        	while True:
        		if output[i] is None and hole_found:
        			output[i] = card
        			break
        		if output[i] is None:
        			hole_found = True
        		i = 0 if i == deck_len-1 else i + 1
        	hole_found = False
        return output

print Solution().deckRevealedIncreasing([17,13,11,2,3,5,21,0,7])
