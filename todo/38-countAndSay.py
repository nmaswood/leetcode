class Solution(object):

    def __init__(self):

        self.d = {
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
        }


    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        n_as_list = str(n)

        l = len(n_as_list)

        if l == 0:
            return []
        elif l ==1 :

            return ['one {}'.format(self.d.get(n))]


        total = 0

        acc = []





        prev = n_as_list[0]

        for num in n_as_list[1:]:

            if num == prev:
                total +=1
            else:

                number_as_word = '{} {}{}'.format(
                    total + 1,
                    self.d.get(int(prev)),
                    's' if total > 1 else ''
                    )

                acc.append(number_as_word)
                total = 0
            prev = num

        if total:

            number_as_word = '{} {}{}'.format(
                total + 1,
                self.d.get(int(prev)),
                's' if total > 1 else ''
                )

            acc.append(number_as_word)




        return acc

r = Solution()

res = r.countAndSay('11123333')

print (res)



        