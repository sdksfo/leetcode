"""
Requirement:

Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.


Algorithm:

Store a hashmap of keys and values, where key is the print string and value is timestamp
If incoming key is not in hashmap, add it to the hashmap with time and return true
If incoming key is available, then update the timestamp and return true if its outside 10 second window, else return false

Complexity:

Time - Hashmap put and get O(1)
Space - O(n)

"""

class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.hashmap:
        	self.hashmap[message] = timestamp
        	return True
        if timestamp - self.hashmap[message] >= 10:
        	self.hashmap[message] = timestamp
        	return True
        return False

# Your Logger object will be instantiated and called as such:
obj = Logger()
print obj.shouldPrintMessage(1,'foo')
print obj.shouldPrintMessage(2,'bar')
print obj.shouldPrintMessage(3,'foo')
print obj.shouldPrintMessage(8,'bar')
print obj.shouldPrintMessage(10,'foo')
print obj.shouldPrintMessage(11,'foo')
