class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-n for n in stones]
        heapq.heapify(minHeap)
        while len(minHeap)>1:
            l1= -heapq.heappop(minHeap)
            l2= -heapq.heappop(minHeap)
            if l1 != l2:
                heapq.heappush(minHeap,-abs(l1-l2))
        return -minHeap[0] if len(minHeap)==1 else 0