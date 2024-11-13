class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res_sum = []

        for i in operations:
            if i == "+":
                temp = res_sum[-1] + res_sum[-2]
                res_sum.append(temp)
            elif i == "D":
                temp = 2 * res_sum[-1]
                res_sum.append(temp)
            elif i == "C":
                res_sum.pop()
            else:
                res_sum.append(int(i))
        return sum(res_sum)
