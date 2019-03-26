

class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split()

        output, vowels, count = [], set('aeiou'), 0

        for word in words:
        	count += 1
        	if word[0].lower() in vowels:
        		output.append(word + 'ma' + 'a'*count)
        	else:
        		output.append(word[1:]+word[0]+'ma'+'a'*count)

        return ' '.join(output)

print Solution().toGoatLatin("ta")
