class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        past_vals = []
        for num in nums:
            if num in past_vals:
                return True
            else:
                past_vals.append(num)
        return False
        