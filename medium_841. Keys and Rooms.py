


class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        def dfs(next_rooms):
            for next_room in next_rooms:
                if not self.visited[next_room]:
                    self.visited[next_room] = True
                    dfs(rooms[next_room])

        self.visited = {room: False for room in xrange(len(rooms))}
        self.visited[0] = True
        dfs(rooms[0])

        return all(self.visited.values())

print Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]])
