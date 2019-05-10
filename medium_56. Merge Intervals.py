

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        output = []

        for interval in sorted(intervals):
        	start, end = interval
        	if output and start <= output[-1][1]:
        		output[-1][1] = max(end, output[-1][1])
        	else:
        		output.append([start, end])

     	return output
