from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0] * len(height)
        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i])

        right_max = [0] * len(height)
        right_max[-1] = height[-1]
        for i in range(len(height)-2, 0, -1):
            right_max[i] = max(right_max[i+1], height[i])

        count = 0
        for i in range(1, len(height)-1):
            count += min(left_max[i], right_max[i]) - height[i]
        return count

    def trap_no_space(self, height: List[int]) -> int:
        left, right, left_max, right_max, count = 0, len(height) - 1, 0, 0, 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    count += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    count += right_max - height[right]
                right -= 1
        return count
