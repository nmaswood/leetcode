# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):

        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        if intervals == []:
            return []

        sorted_list = sorted(intervals, key = lambda x: x.start)

        def recurse(List,previousLen):

            l = len(List)

            if l < 2:
                return List
            elif l == previousLen:
                return List
            else:

                acc = []
                skip = False

                for index, interval in enumerate(intervals[:-1]):

                    if not skip and index + 2 == l:
                        acc.append(intervals[index + 1])

                    if not skip:

                        nextInterval = intervals[index + 1]

                        first, second = interval.start, interval.end

                        third, fourth = nextInterval.start, nextInterval.end

                        if second == third:
                            acc.append((first, fourth))
                            skip = True

                        elif abs(second - third) == 1:
                            acc.append((first, fourth))
                            skip = True

                        acc.append(interval)
                    else:
                        skip = False
                return recurse(acc, l)

        return recurse(sorted_list, -1)


x = [[1,3],[2,6],[8,10],[15,18]]
exp = [[1,6],[8,10],[15,18]]



r = Solution()

res = r.merge([])
print (res)
        