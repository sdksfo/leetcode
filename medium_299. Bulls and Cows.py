

class Solution(object):
    def getUnmatched(self, secret, guess):
        cows, i, j, secret, guess = 0, 0, 0, sorted(secret), sorted(guess)

        while i < len(secret) and j < len(guess):
            if secret[i] == guess[j]:
                cows += 1
                i += 1
                j += 1
            elif secret[i] < guess[j]:
                i += 1
            else:
                j += 1

        return cows

    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls, missing_secret, missing_guess = 0,  [], []

        for idx in xrange(len(secret)):
            if secret[idx] == guess[idx]:
                bulls += 1
            else:
                missing_secret.append(secret[idx])
                missing_guess.append(guess[idx])

        cows = self.getUnmatched(missing_secret, missing_guess)

        return '%sA%sB' %(bulls, cows)

print Solution().getHint('1807', '7810')
