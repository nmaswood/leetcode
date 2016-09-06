class Solution(object):

    def ones(self, num):
        return {
            0:'',
            1:'I',
            2:'II',
            3:'III',
            4:'IV',
            5:'V',
            6:'VI',
            7:'VII',
            8:'VIII',
            9:'IX',
        }[num]

    def tens(self, num):
        return {
            0:'',
            1:'X',
            2:'XX',
            3:'XXX',
            4:'XL',
            5:'L',
            6:'LX',
            7:'LXX',
            8:'LXXX',
            9:'XC',
        }[num]

    def hundreds(self, num):
        return {
            0:'',
            1:'C',
            2:'CC',
            3:'CCC',
            4:'CD',
            5:'D',
            6:'DC',
            7:'DCC',
            8:'DCCC',
            9:'CM',
        }[num]

    def thousand(self, num):
        return {
            0:'',
            1:'M',
            2:'MM',
            3:'MMM'
        }[num]


    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        assert num > 0
        ori = num

        acc = []


        for i,f in enumerate([self.ones, self.tens, self.hundreds, self.thousand]):
            print (num)

            if num <= 0:
                break

            rem = num % 10
            acc.append(f(rem))
            num /= 10
            num = int(num)

        res = ''.join(acc[::-1])

        return res


#r = Solution()
#r.intToRoman(1800)
#r.intToRoman(900)
#r.intToRoman(1)
