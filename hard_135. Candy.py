
# Approach 1: Do a two pass on forward and reverse direction and greedily compute candies that can be given

# Rules for assigning candies:

# a) If the current number is lesser than either side, assign 1 candy
# b) If a candy/candies is already assigned to somebody on ur left and ur rating is lesser than person on ur right, its safe
#    to assume we can provide one candy more than person on ur left. And likewise for right person also

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        ratings, output = [float('inf')] + ratings + [float('inf')], [0] * (len(ratings)+2)

        for j in [range(len(ratings)-2, 0, -1), range(1, len(ratings)-1)]:
            for i in j:
                if ratings[i-1] >= ratings[i] <= ratings[i+1]:
                    output[i] = 1
                else:
                    if (output[i-1] and output[i+1]):
                        output[i] = max(output[i-1], output[i+1]) + 1
                    if (output[i-1] and ratings[i] <= ratings[i+1]):
                        output[i] = output[i-1] + 1
                    if (output[i+1] and ratings[i] <= ratings[i-1]):
                        output[i] = output[i+1] + 1

        return sum(output[1:-1])
