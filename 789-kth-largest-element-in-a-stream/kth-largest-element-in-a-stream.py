class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap,self.k = nums,k
        #create min heap using below method
        heapq.heapify(self.minHeap)
        #remove all the min elements from heap to maintain the kth large element
        while len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        #add new element to heap
        heapq.heappush(self.minHeap,val)
        #if the len is more then k, then remove the min element
        if len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)
        #0th index of heap always stores the kth largest element of heap
        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)