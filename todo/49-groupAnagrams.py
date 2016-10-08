class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        sorted_strs = [(x, sorted(x)) for x in strs]

        only_sorted = set(sorted(x) for x in strs)

        vals = {x:[] for x in only_sorted}


        for original, sorted_str in sorted_strs:

            vals[sorted_str].append(original)

        acc = []

        return vals.values()
