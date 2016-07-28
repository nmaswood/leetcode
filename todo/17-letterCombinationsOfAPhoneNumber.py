class Tree():
    def __init__(self,root):
        self.root = root
        self.children = None

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
        }[char].split()

    def num_str_to_char_list(self, num_str):

        return [self.num_to_char(num) for num in num_str.split()]


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

        def tree_to_str(self,tree):

            foo = []

            def sub(tree, acc):

                if tree in [None, "", []]:
                    foo.append(acc)

                root = tree.root

                new_letters = [root + x for x in acc]

                for child in self.children:
                    return sub(child, acc)

                return acc

            print sub(tree, [''])
