class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashi={}
        for n,i in enumerate(nums):
            diff=target-i
            if diff in hashi:
                return [hashi[diff],n]
            hashi[i]=n