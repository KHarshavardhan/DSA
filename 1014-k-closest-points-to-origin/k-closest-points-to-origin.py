class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        res = []
        #to find the distance between a,b from origin 0,0 can be done using a2 + b2 = c2 formula
        for a,b in points:
            dist = (a**2)+(b**2)
            dist = dist**(0.5)
            arr.append([dist,a,b])
        #created arr and now create min heap with key as dist , which automatically sorts on dist
        heapq.heapify(arr)
        while k>0:
            dist,a,b = heapq.heappop(arr)
            res.append([a,b])
            k-=1
        return res