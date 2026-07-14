class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        past_vals = set()
        for num in nums:
            if num in past_vals:
                return True
            else:
                past_vals.add(num)
        return False
        