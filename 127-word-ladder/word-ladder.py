class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nc = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+'*'+word[i+1:]
                nc[pattern].append(word)
        visit=set([beginWord])
        q=deque([beginWord])
        res=1

        while q:
            for i in range(len(q)):
                word=q.popleft()
                if word==endWord:
                    return res
                for x in range(len(word)):
                    pattern = word[:x]+'*'+word[x+1:]
                    for j in nc[pattern]:
                        if j not in visit:
                            visit.add(j)
                            q.append(j)
            res+=1
        return 0