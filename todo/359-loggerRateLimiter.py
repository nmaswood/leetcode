TEN_SECONDS = 10000

class Logger(object):

    def __init__(self):

        self.d = {}

    def _check_(self, word,ts):

        temp = self.d.get(word,0)
        self.d[word] = ts

        return temp

    def _should_print(self, word,ts):

        return self._check_(word,ts) >= TEN_SECONDS


    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """

        if self._should_print(word, timestamp):
            print (message)


        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)