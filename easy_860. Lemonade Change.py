

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        currencies = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            currencies[bill] += 1
            change = bill - 5

            for i in [10, 5]:
                if change and change >= i and currencies[i] >= change/i:
                    currencies[i] -= change/i
                    change %= i

            if change: return False

        return True

print Solution().lemonadeChange([5,5,5,5,5,5,5,5,20,20,20])
