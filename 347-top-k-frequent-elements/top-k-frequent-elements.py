class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        setNums = set(nums)
        dict_count = {}
        result = []
        for i in setNums:
            dict_count[i]= nums.count(i)
        for x in range(k):
            result.append(max(dict_count,key=lambda item:dict_count[item]))
            dict_count.pop(max(dict_count,key=lambda item:dict_count[item]))
        return result
