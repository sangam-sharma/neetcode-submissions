class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s=stones
        s=[-x for x in s]
        heapq.heapify(s)
        while len(s)>1:
            first = -heapq.heappop(s)
            second=-heapq.heappop(s)
            if first!=second:
                heapq.heappush(s,-(first-second))
        return abs(s[0]) if s else 0



        