class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        gas_total = 0
        for gas_new, cost_new in zip(gas, cost):

            gas_total += (gas_new - cost_new)

            if gas_total < 0:
                return -1
        return 0

