class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        dummy=[]
        for i in nums:
            dummy.append(i)
        for i in nums:
            dummy.append(i)
        return dummy