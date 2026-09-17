class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            count[i]= 1+count.get(i,0)
        heap=[]
        res=[]
        for i in count:
            heapq.heappush(heap,(count[i],i))
        while len(heap)>k:
            heapq.heappop(heap)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

            
            

            
        