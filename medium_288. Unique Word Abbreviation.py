import collections

class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.dictionary = dictionary
        self.dict2 = collections.defaultdict(set)

        for word in dictionary:
            abv = self.getAbv(word)
            self.dict2[abv].add(word)

    def getAbv(self, word):
        if len(word) > 2:
            abv = word[0] + str(len(word) - 2) + word[-1]
        else:
            abv = word
        return abv

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        abv = self.getAbv(word)
        val = self.dict2[abv]
        return len(val) == 0 or (len(val) == 1 and next(iter(val)) == word)
