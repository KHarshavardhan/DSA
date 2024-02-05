class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = []
        result=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while temp and temperatures[temp[-1]]<temperatures[i]:
                top = temp.pop()
                result[top] = i-top
            temp.append(i)
        return result
                

