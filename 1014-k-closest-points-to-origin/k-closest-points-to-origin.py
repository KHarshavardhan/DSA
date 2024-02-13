class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        res = []
        for a,b in points:
            dist = (a**2)+(b**2)
            dist = dist**(0.5)
            arr.append([dist,a,b])
        heapq.heapify(arr)
        while k>0:
            dist,a,b = heapq.heappop(arr)
            res.append([a,b])
            k-=1
        return res