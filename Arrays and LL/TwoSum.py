from typing import List

class Solution:
    ### O(N^2) way ###
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index_one in range(len(nums)):
            for index_two in range(len(nums)):
                if index_one == index_two:
                    pass
                elif (nums[index_one] + nums[index_two]) == target:
                    return [index_one, index_two]
    ### O(N) way ###
    def optimalTwoSum(self, nums: List[int], target: int) -> List[int]:
        # Idea: look for the complement using a dictionary since searching in dictionary is O(1)
        dic = {}
        index_lst = []
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = set([i])
            else:
                dic[nums[i]].add(i)

        for index in range(len(nums)):
            complement = target - nums[index]
            # compleement is another number
            if complement in dic and complement != nums[index]:
                index_lst.append(index)
            # complement is itself
            elif complement in dic and len(dic[complement]) > 1:
                index_lst.append(index)

        return index_lst



solution = Solution()
nums = [2,7,11,15]
target = 9
print(f"Naive Solution: {solution.twoSum(nums, target)}")
print(f"Optimal Solution: {solution.optimalTwoSum(nums, target)}")

nums = [3,2,4]
target = 6
print(f"Naive Solution: {solution.twoSum(nums, target)}")
print(f"Optimal Solution: {solution.optimalTwoSum(nums, target)}")

nums = [3,3]
target = 6
print(f"Naive Solution: {solution.twoSum(nums, target)}")
print(f"Optimal Solution: {solution.optimalTwoSum(nums, target)}")