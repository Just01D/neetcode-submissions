class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 1
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[start] = nums[r]
                start+=1

        return start