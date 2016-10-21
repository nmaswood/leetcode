from collections import defaultdict
from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        MAX_INT = 2147483647

        start = 0
        end = 0

        char_need = Counter(t)   # the count of char needed by current window, negative means current window has it but not needs it
        count_need = len(t)             # count of chars not in current window but in t

        min_length = MAX_INT
        min_start = 0

        while end < len(s):

            current_char = s[end]

            if char_need[current_char] > 0:
                count_need -= 1
            # current window contains s[end] now, so does not need it any more
            print (s[end])

            char_need[current_char] -= 1      
            end += 1

            while count_need == 0:
                distance = end - start

                if min_length > distance:
                    min_length = distance
                    min_start = start
                start_char  = s[start]
                char_need[start_char] += 1    
                # when some count in char_need is positive, it means there is char in t but not current window
                if char_need[start_char] > 0: 
                    count_need += 1
                start += 1
        return "" if min_length == MAX_INT else s[min_start:min_start + min_length]


if __name__ == "__main__":
    r = Solution()
    res = r.minWindow("ADOBECODEBANC", "ABC")
    print (res)
