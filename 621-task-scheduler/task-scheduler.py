class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        minHeap = [-n for n in c.values()]
        heapq.heapify(minHeap)
        q= deque()
        time=0
        print(minHeap)
        while minHeap or q:
            time+=1
            if minHeap:
                temp = 1 + heapq.heappop(minHeap)
                if temp:
                    q.append([temp,time+n])
            if q and q[0][1]==time:
                heapq.heappush(minHeap,q.popleft()[0])
        return time