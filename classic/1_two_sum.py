from typing import List


class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                return [i, dic[target - nums[i]]]
            else:
                dic[nums[i]] = i

        return [-1, -1]



