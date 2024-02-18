class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        minHeap = []
        res=[]
        for i in c:
            minHeap.append([-c[i],i])
        heapq.heapify(minHeap)
        while k>0:
            count,n = heapq.heappop(minHeap)
            res.append(n)
            k-=1
        return res