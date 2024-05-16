class Solution(object):
    def __init__(self):
        self.ans = []

    def helper(self, candidates, target, index, lst):
        if target == 0:
            self.ans.append(lst[:])
            return
        if index == len(candidates) or target < 0:
            return
        
        # Exclude the current candidate
        self.helper(candidates, target, index + 1, lst)
        
        # Include the current candidate
        lst.append(candidates[index])
        self.helper(candidates, target - candidates[index], index, lst)
        lst.pop()
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.ans = []  # Clear the ans list before starting a new computation
        self.helper(candidates, target, 0, [])
        return self.ans