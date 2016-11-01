s = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"


class Tree():


    def __init__(self,val, children = []):
        self.val = val
        self.children = children


class Solution(object):


    def parse(self, raw_str,tree_so_far ):

        if not raw_str:
            return tree_so_far

        first, rest = raw_str[0], rest[1:]

        if first.startswith("\t"):

            return parse(
                rest,
                rtree_so_far.children.append(first.lstrip("\t"))
                )
        else:


            return self.parse(
                rest, 
                tree_so_far.chidren.append()




                )








    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        pass        

        fo


splat = s.split("\n")
print (splat)

for l in splat:
    print (l)