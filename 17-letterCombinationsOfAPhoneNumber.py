class Tree():

    def __init__(self,root):
        self.root = root
        self.children = []

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.root)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def __repr__(self):
        return '<tree node representation>'

class Solution(object):

    def num_to_char(self, char):
        return {
            "0": "_",
            "1": None,
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }[char]

    def num_str_to_char_list(self, num_str):

        return [list(self.num_to_char(num)) for num in list(num_str)]

    def letterCombinations(self, digits):

        """
        :type digits: str
        :rtype: List[str]
        """

        def process_tree(tree, list_of_char_list):

            if len(list_of_char_list) == 0:
                return tree

            first = list_of_char_list[0]
            rest = list_of_char_list[1:]

            for letter in first:
                new_tree = process_tree(Tree(letter), rest)
                tree.children.append(new_tree)

            return tree

        def tree_to_str(tree, acc):

            root = tree.root
            children = tree.children

            if not children:
                return [x + root for x in acc]
            else:
                f = []
                for child in children:
                    d = tree_to_str(child, [x + root for x in acc])
                    f.append(d)
                return f

        def flatten(S):
            if S == []:
                return S
            if isinstance(S[0], list):
                return flatten(S[0]) + flatten(S[1:])
            return S[:1] + flatten(S[1:])

        if digits == "":
            return []

        as_list_of_lists = self.num_str_to_char_list(digits)

        processed_tree = process_tree(Tree(""), as_list_of_lists)

        strs = tree_to_str(processed_tree, [''])
        return flatten(strs)


#r = Solution()
# print (r.letterCombinations('23'))

# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].



