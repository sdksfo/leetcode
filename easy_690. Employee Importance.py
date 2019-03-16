
"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution(object):
    def dfs(self, employees, empid, seen):
        if empid not in seen:
            seen.add(empid)
            return employees[empid].importance + sum(self.dfs(employees, x, seen) for x in employees[empid].subordinates)

    def getImportance(self, employees, empid):
        return self.dfs({emp.id: emp for emp in employees}, empid, set())
