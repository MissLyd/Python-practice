class Solution(object):
    def minSubArrayLen(self, target, nums):
        l=0; sum=0
        min_len= float("inf")
        
        for r in range(len(nums)): 
            sum += nums[r]
            print(f"sum:{sum}")

            while sum >= target:
                min_len=min(min_len,r-l+1)
                sum-=nums[l]
                l+=1

        return 0 if min_len==float("inf") else min_len
    
sol = Solution()
target = 7
nums = [2,3,1,2,4,3]
        
sub = sol.minSubArrayLen(target,nums)

print(sub)