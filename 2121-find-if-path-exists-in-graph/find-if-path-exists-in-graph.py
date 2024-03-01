class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        q = deque()
        visit = set()
        found = False
        visit.add(source)
        q.append(source)
        while q:
            for i in range(len(q)):
                c = q.popleft()
                if c == destination:
                    return True
                for a,b in edges:
                    if c in [a,b] and (a not in visit or b not in visit):
                        if a not in visit:
                            q.append(a)
                            visit.add(a)
                        else:
                            q.append(b)
                            visit.add(b)

        return found