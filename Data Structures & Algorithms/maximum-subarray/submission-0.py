class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr,maxi=0,nums[0]
        for num in nums:
            if curr < 0:
                curr=0
            curr+=num
            maxi=max(maxi,curr)
        return maxi

        