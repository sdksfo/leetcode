
# Approach 1: TLE. Create an array of arrays. For each number encountered, either add it to any of the existing sequences if it can be added (ie if consecutive)
# else start a new series.

class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp = []

        for num in nums:
            for i in xrange(len(temp)-1, -1, -1):
                end_num, count = temp[i]
                if num - end_num == 1:
                    temp[i] = [num, count+1]
                    break
            else:
                temp.append([num, 1])

        return all([i[1] > 2 for i in temp])

# Approach 2: Optimized the above by using a hashmap and short circuiting if the number atleast 3 nums before has a count less than 3. This barely passes LC

class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp, hashmap = [], {}

        for num in nums:
            if num - 3 in hashmap and hashmap[num-3] < 3:
                return False
            for i in xrange(len(temp)-1, -1, -1):
                start_num, end_num, count = temp[i]
                if num - end_num == 1:
                    temp[i] = (start_num, num, count+1)
                    hashmap[start_num] = count+1
                    break
            else:
                hashmap[num] = 1
                temp.append([num, num, 1])

        return all([i[2] > 2 for i in temp])
