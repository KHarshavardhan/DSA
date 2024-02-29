class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #edge case when word is not present return 0
        if endWord not in wordList:
            return 0
        #create neighbour collection-hashmap--> use this to auto add empty value when key is added
        nc = collections.defaultdict(list)
        #make sure that word is inside the wordlist 
        wordList.append(beginWord)
        #creating hashmap of words with same letters as other words with wildcard 
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+'*'+word[i+1:]
                nc[pattern].append(word)
        #visit to mark used words and queue to go through the graph layer by layer
        visit=set([beginWord])
        q=deque([beginWord])
        res=1
        while q:
            #every layer of words, it goes through, increment res value--> path
            for i in range(len(q)):
                word=q.popleft()
                if word==endWord:
                    return res
                #for each word, create pattern, check in hashmap and if found match append to queue and visit
                for x in range(len(word)):
                    pattern = word[:x]+'*'+word[x+1:]
                    for j in nc[pattern]:
                        if j not in visit:
                            visit.add(j)
                            q.append(j)
            res+=1
        return 0