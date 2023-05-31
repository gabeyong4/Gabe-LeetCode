'''
Naive Solution O(N): going thru the whole array to check for duplicates
'''
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tracker = set()
        for i in nums:
            if i not in tracker:
                tracker.add(i)
            else:
                return True
        return False
