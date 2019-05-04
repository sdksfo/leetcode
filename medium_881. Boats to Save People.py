
# Since the capacity is 2, we try to load the biggest and smallest person. If not just load the biggest person

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        boats, p = 0, sorted(people)

        i, j = 0, len(p)-1

        while i <= j:
            if p[i] + p[j] <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
            boats += 1
        return boats

# If capacity is not restrictive, try to load as many big persons as possible followed by as many small
# person as possible until limit is reached.

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        boats, p = 0, sorted(people)

        i, j = 0, len(p)-1

        while i <= j:
            capacity, total = 0, 0
            while total + p[j] <= limit and capacity < 2:
                total += p[j]
                j -= 1
                capacity += 1
            while total + p[i] <= limit and capacity < 2:
                total += p[i]
                i += 1
                capacity += 1
            boats += 1

        return boats

print Solution().numRescueBoats([2,2,2,3,3], 6)
