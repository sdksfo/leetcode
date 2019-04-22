"""
Plain vanilla binary search for a number. Just that when outofbounds is encountered reset the 'high' index.
"""

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        i, j = 0, 10000

        while i < j:
        	mid = i + (j-i)/2

        	element = reader.get(mid)

        	if element == target:
        		return mid
        	elif element > target or element == 2147483647:
        		j = mid
        	else:
        		i = mid + 1

        return -1
