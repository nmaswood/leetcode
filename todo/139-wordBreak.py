class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """

        l = len(s)

        if l == 0:
            return False

        DT = [False for _ in range(l +  1)]
        DT[0] = True

        for i in range(1, l+ 1):

            for j in range(1,l + 1):

                sub_str = s[i-1:j]
                print(sub_str)

                if sub_str in wordDict:
                    if DT[i-1]:
                        DT[j] = True
                        break
        print (DT)

        return DT[-1]


s = "aaaaaaa"
d = set(["aaaa","aaa"])

r = Solution()

res = r.wordBreak(s,d)
print (res)