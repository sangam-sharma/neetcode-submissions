class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        maxindex=0
        for i in range(n):
            if maxindex<i:
                return False
            maxindex=max(maxindex,i+nums[i])
        return True
            
            


        