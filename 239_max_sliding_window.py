# First solution

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        l=0
        r=k-1
        max_array=[]
        max_obj=nums[l]
        while r<len(nums):
            for i in range(l,r+1):
                max_obj=max(max_obj,nums[i])
            max_array.append(max_obj)
            l+=1; r+=1
        
        return max_array
    
sol = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(sol.maxSlidingWindow(nums,k))

# Second solution

from collections import deque 

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        dq= deque()
        max_array=[]
        l = r = 0

        while r<len(nums):
            # while dq exists and the element we added is greater than the last element of the queue
            while dq and nums[dq[-1]] < nums[dq]:
                # pop the last element
                dq.pop()
                # add the new element
            dq.append(r)

            # if the first element of our window is greater than the first element of our queue
            if l>dq[0]:
                # pop it
                dq.popleft()

            # when our window reaches desired size
            if (r+1)>=k:
                # we append the first element of the queue since it"s the greatest
                max_array.append(nums[dq[0]])
                # only then do we increment l
                l+=1
            r+=1

        return max_array

        
sol = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(sol.maxSlidingWindow(nums,k))