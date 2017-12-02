class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        up_down = 0
        left_right = 0

        up_down_set = {'U', 'D'}

        for move in moves:

            if move == 'U':
                up_down += 1
            elif move == 'D':
                up_down -= 1
            elif move == 'L':
                left_right += 1
            else:
                left_right -= 1

        return up_down == 0 and left_right == 0
