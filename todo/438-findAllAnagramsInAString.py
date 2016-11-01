from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        acc = []

        len_s =  len(s)
        len_p = len(p)


        if len_s < len_p:

        	if len_s == len_s:
        		return [0]
        	return []

        p_counted = Counter(p)

        for i in range(len_s):

        	str_prime = s[i:i+len_p]
        	if not str_prime:
        		return acc
        	s_counted = Counter(str_prime)

        	if s_counted == p_counted:
        		acc.append(i)

        return acc

s = "abab"; p =  "ab";
r = Solution()

res = r.findAnagrams(s, p)
print (res)

