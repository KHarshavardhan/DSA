class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #append 0 to the end of cost to set destination
        cost.append(0)
        #from last 3rd element, check the min of next two elements and add to current.
        for i in range(len(cost)-3,-1,-1):
            cost[i]=cost[i]+min(cost[i+1],cost[i+2])
        #remove added extra 0
        cost.pop(len(cost)-1)
        #result will be minimum of first and second element
        return min(cost[0],cost[1])