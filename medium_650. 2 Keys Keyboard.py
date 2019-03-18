
"""

a) For getting 'n' chars on screen, its 1 + min(copy_curr_char, paste_already_copied)
b) If chars on screen goes over 'n' chars, abort and return sys.maxint
c) How do i know, how many is in the buffer ?. So i have to pass the copied chars to the function signature,
so that the paste operation would tell me how many more is needed

Atleast two steps are mandatorily required. ie copy the 'A' already in the screen and paste it.
The program begins execution from the 3rd step. Two possibilities exist from here:
a) Either continue pasting the copied character, in which case the total chars on screen is t+c where 't' is total chars existing before the paste and 'c' is the number of copied chars
b) Or copy the chars that are on the screen. This makes the current chars on screen as t*2 since we have copied all and then pasted them.

"""

class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}

        def calcSteps(c, t):
            if (c, t) not in cache:
                if n == t:
                    return 0
                if t > n:
                    return float('inf')
                cache[c, t] = min(1 + calcSteps(c, t+c), 2 + calcSteps(t, t*2))
            return cache[c, t]

        return 2 + calcSteps(1, 2) if n > 1 else 0
