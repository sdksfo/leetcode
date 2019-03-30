
class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.hashmap = set(range(maxNumbers))

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        return self.hashmap.pop(0) if self.hashmap else -1

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return number in self.hashmap

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: None
        """
        self.hashmap.add(number)
