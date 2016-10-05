from queue import Queue

class LRUCache(object):

    def __init__(self, capacity):

        """
        :type capacity: int
        """

        self.values_counter = {}
        self.queue = Queue()



    def set(self, key):

        """
        :rtype: int
        """
        if self.queue.full():

            removed = self.queue.get()
            values = self.values_dictonary[removed]

            if values == 1:
                del values_dictionary[removed]
            else:
                values_dictionary[removed] -= 1
        else:
            current = values_dictionary.get(removed, 0)
            values_dictionary = current + 1

        self.queue.put(key)
        values_dictionary[key] = values_dictionary.get(key) + 1


    def get(self, key, value):

        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        inDict = key in self.values_dictonary:
        self.set(key)

        if not inDict:
            return -1
        return key
