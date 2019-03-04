
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        def preprocess_name(name):
        	name = name.split('+')[0]
        	name = ''.join(name.split('.'))
        	return name

        uniques = set()

        for email in emails:
        	name, domain = email.split('@')
        	updated_name = preprocess_name(name)
        	uniques.add(updated_name+'@'+domain)

        return len(uniques)

print Solution().numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
