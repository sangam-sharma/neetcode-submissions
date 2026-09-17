class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index=0
        count=[0]*3
        for i in range(len(nums)):
            count[nums[i]]+=1
        for i in range(3):
            while count[i]:
                count[i]-=1
                nums[index]=i
                index+=1




       