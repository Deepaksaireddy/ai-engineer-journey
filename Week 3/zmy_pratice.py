#1. Leet code
#Valid anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False

#2 sum
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i


# Contains Duplicate
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