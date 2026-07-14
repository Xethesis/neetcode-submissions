class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            needed_num = target - num
            if needed_num in nums_dict:
                return[nums_dict[needed_num], i]
            nums_dict[num] = i