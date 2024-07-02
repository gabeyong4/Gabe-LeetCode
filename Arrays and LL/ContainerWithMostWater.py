from typing import List

class Solution:
    ### O(N^2) Solution ###
    def maxArea(self, height: List[int]) -> int:
        max = 0
        for index_one in range(len(height)):
            for index_two in range(len(height)):
                # print(index_one)
                # print(index_two)
                width = self._min(height[index_one], height[index_two])
                # print(f'width is :{width}')
                length = abs(index_one - index_two)
                # print(f'length is: {length}')
                curr_max = width * length
                if curr_max > max:
                    max = curr_max
        return max
    
    def optimalMaxArea(self, height: List[int]) -> int:
        # Idea:
        # two pointers starting from the max length on the Left and Right side
        # always try to maximise the width.
        left_pos = 0
        right_pos = len(height)-1
        left = height[left_pos]
        right = height[right_pos]
        length = len(height) - 1
        maxArea = 0
        while left_pos != right_pos:
            width = self._min(left, right)
            area = width * length
            if area > maxArea:
                maxArea = area
            # decide which pointer should move inwards
            # 1. if one width higher than the other, the one with the lower width should move inwards
            # 2. if both same width, find which pointer.next() is higher.
            left_pos, right_pos = self._decide_pointer_movement(left_pos, right_pos, height)
            left = height[left_pos]
            right = height[right_pos]
            length -= 1
        return maxArea
    
    def solutionMaxArea(self, height: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(height)-1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            maxArea = max(area, maxArea)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea
            
    def _decide_pointer_movement(self, left_pos, right_pos, height):
        if height[left_pos] > height[right_pos]:
            right_pos -= 1
        elif height[right_pos] > height[left_pos]:
            left_pos += 1
        else:
            left_pos += 1
        return left_pos, right_pos

    def _min(self, num1, num2) -> int:
        arr = [num1, num2]
        return min(arr)
    
solution = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(solution.maxArea(height))
print(solution.optimalMaxArea(height))

height = [1,1]
print(solution.maxArea(height))
print(solution.optimalMaxArea(height))