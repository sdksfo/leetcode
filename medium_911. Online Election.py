import collections

class TopVotedCandidate:

    def __init__(self, persons, times):
        c = collections.Counter()
        self.persons, curr, self.times = [], 0, times
        for person in persons:
            c[person] += 1
            if c[person] >= curr:
                curr, cand = c[person], person
            self.persons.append(cand)

    def q(self, t):
        low, high = 0, len(self.persons) - 1
        while low <= high:
            mid = (high+low)/2
            if self.times[mid] <= t:
                person = self.persons[mid]
                low = mid + 1
            else:
                high = mid - 1
        return person

obj = TopVotedCandidate([0,0,0,0,1],[0,6,39,52,75])

for cm in [[45],[49],[59],[68],[42],[37],[99],[26],[78],[43]]:
    print obj.q(cm[0])
