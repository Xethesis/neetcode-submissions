class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed_dict = {}
        for i, num in enumerate(nums):
            needed_num = target - num
            if needed_num in needed_dict:
                return [needed_dict[needed_num],i]
            needed_dict[num] = i
