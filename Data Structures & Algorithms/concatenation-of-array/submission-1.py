class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        dummy=[0]*(2*n)
        for i,num in enumerate(nums):
            dummy[i]=dummy[i+n]=num
        return dummy
        