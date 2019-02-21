
"""Basically the idea is to group similar accounts together. For each email-id encountered, assign its parent as the name"""


from collections import defaultdict

class Solution(object):

    def getParent(self, n):
        if n in self.parent:
            return self.getParent(self.parent[n])
        return n

    def union(self, child, parent):
        if child != parent:
            self.parent[child] = parent

    def groupEmails(self):
        temp = defaultdict(list)
        for email, name in self.parent.items():
            if '@' in email:
                temp[self.getParent(name)].append(email)
        return [[name.split('-')[0]] + sorted(temp[name]) for name in temp]

    def accountsMerge(self, accounts):
        self.parent, ctr = {}, 0
        for account in accounts:
            name, emails, ctr = account[0], account[1:], ctr+1
            name += '-' + str(ctr)
            for email in emails:
                if email not in self.parent:
                    self.union(email, name)
                else:
                    old_parent = self.getParent(email)
                    self.union(old_parent, name)
        return self.groupEmails()

print Solution().accountsMerge([["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]])
