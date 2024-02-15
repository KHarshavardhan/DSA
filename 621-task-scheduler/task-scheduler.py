class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #Counter will count all the unique values and their occurences in a hashmap i.e count
        count = Counter(tasks)
        #Creating a maxHeap Heap which will have the count of unique var occurences
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        #deque is used to store the use of a var and its next possible usage time i.e time+n
        q = deque()
        time = 0
        while maxHeap or q:
            time +=1
            #if heap still has elements, we check reduce the count and add it to q(deque) with time
            if maxHeap:
                e = 1 + heapq.heappop(maxHeap)
                if e:
                    q.append([e,time+n])
            # if left most element in queue has current time, we will pop it out and add back to heap 
            if q and q[0][1]==time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time

