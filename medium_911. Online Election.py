import collections


class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.winners, self.times = [], times
        vote_count, counts = 0, collections.defaultdict(int)

        for person in persons:
            counts[person] += 1
            if counts[person] >= vote_count:
                vote_count = counts[person]
                winner = person
            self.winners.append(winner)

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        i, j = 0, len(self.times)

        while i < j-1:
            mid = i + (j-i)/2
            if self.times[mid] <= t:
                i = mid
            else:
                j = mid

        return self.winners[i]
