class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        self.len = len(set(nums))
        self.length = len(nums)
        if self.len == self.length:
            return False
        else:
            return True

sol = Solution()

print(sol.containsDuplicate([1,2,3,4]))