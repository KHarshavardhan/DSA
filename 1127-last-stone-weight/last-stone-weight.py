class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #python doesnt have the max heap to convert pos num to neg nums and use it
        stones = [-s for s in stones]
        #heapq.heapify will convert the list into min heap
        heapq.heapify(stones)
        while (len(stones)>1):
            #a,b will have values of the latest removed max numbers 
            a=abs(heapq.heappop(stones))
            b=abs(heapq.heappop(stones))
            #if a,b are not equal, adds the diff back into the heap
            if a!=b:
                heapq.heappush(stones,-(abs(a-b)))
        return abs(stones[0]) if len(stones) != 0 else 0
