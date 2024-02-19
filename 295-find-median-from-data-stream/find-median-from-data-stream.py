class MedianFinder:

    def __init__(self):
        self.first = []
        self.sec = []
        heapq.heapify(self.first)
        heapq.heapify(self.sec)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.first,-num)
        if self.first or self.sec:
            if self.sec and -self.first[0]>self.sec[0]:
                heapq.heappush(self.sec,-heapq.heappop(self.first))
            if len(self.first)-len(self.sec)>1:
                heapq.heappush(self.sec,-heapq.heappop(self.first))
            if len(self.sec)-len(self.first)>1:
                heapq.heappush(self.first,-heapq.heappop(self.sec))
            

    def findMedian(self) -> float:
        if len(self.first)==len(self.sec):
            return (-self.first[0]+self.sec[0])/2
        else:
            if len(self.first)>len(self.sec):
                return -self.first[0]
            else:
                return self.sec[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()