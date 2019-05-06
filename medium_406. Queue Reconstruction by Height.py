
# Approach 1: Sort by height from highest to lowest. Insert the highest person into the output.
# And for each person iterate through the output array and determine the insert position based on
# how many are in front of them.

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        output, people = [], sorted(people, key=lambda (h, k): (-h, k))

        for p in people:
            i, expected = 0, p[1]
            while i < len(output) and expected:
                if output[i][0] >= p[0]:
                    expected -= 1
                i += 1
            output.insert(i, p)

        return output

# Approach 2: spochmann's solution. Each time a person is placed we use the person[1] to tell
# us the insert position, as there are that many people in the queue at that point infront of
# him. details: https://leetcode.com/problems/queue-reconstruction-by-height/discuss/89359/Explanation-of-the-neat-Sort%2BInsert-solution

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        output, people = [], sorted(people, key=lambda (h, k): (-h, k))

        for p in people:
            output.insert(p[1], p)

        return output
