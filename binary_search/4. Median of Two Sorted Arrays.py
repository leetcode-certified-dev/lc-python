from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # use binary search in a shorter list
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        # position of  |
        left, right = 0, len(nums1)
        while left <= right:
            par1 = int((left + right) / 2)
            if par1 == 0:
                left_max_1 = float("-inf")
            else:
                left_max_1 = nums1[par1-1]

            if par1 == len(nums1):
                right_min_1 = float("inf")
            else:
                right_min_1 = nums1[par1]

            par2 = int((len(nums1) + len(nums2) + 1) / 2) - par1
            if par2 == 0:
                left_max_2 = float("-inf")
            else:
                left_max_2 = nums2[par2 - 1]

            if par2 == len(nums2):
                right_min_2 = float("inf")
            else:
                right_min_2 = nums2[par2]

            if left_max_1 <= right_min_2 and left_max_2 <= right_min_1:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(left_max_1, left_max_2) + min(right_min_1, right_min_2)) / 2
                else:
                    return max(left_max_1, left_max_2)
            elif left_max_1 > right_min_2:
                right = par1 - 1
            else:
                left = par1 + 1
        return -1
