
class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        total, temp, i = 0, ['']*4, 0
        char_count = read4(temp)

        while n > 0 and char_count:
            total += char_count
            for j in xrange(min(char_count, n)):
                buf[i] = temp[j]
                i += 1
            temp = ['']*4
            n -= char_count
            char_count = read4(temp)

        buf[:] = buf[:i]

        return total
