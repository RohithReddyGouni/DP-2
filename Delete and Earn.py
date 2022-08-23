#Time Complexity: O(n)
#Space Complexity: O(max(nums))

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        Total_Array=[0]*(max(nums)+1);
        
        for value in nums:
            Total_Array[value]+=value;
        
        dp=[0]*len(Total_Array);
        dp[1]=Total_Array[1];
        for i in range(2,len(dp)):
            dp[i]=max(dp[i-1],Total_Array[i]+dp[i-2]);
        
        return dp[-1];