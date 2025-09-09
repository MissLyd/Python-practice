# First solution
class Solution(object):
    def findLength(self, nums1, nums2):
        l1=r1=0
        max_len=float("-inf")

        while r1<len(nums1):
            # Pointer that will go through nums2
            l2=0
            while l2<len(nums2):
                cur_len=0
                i,j=r1,l2
                while i<len(nums1) and j<len(nums2) and nums1[i]==nums2[j]:
                    cur_len+=1
                    i += 1; j+=1
                max_len = max(max_len,cur_len)
                l2+=1
            r1+=1

        return 0 if max_len==float("-inf") else max_len
    

sol = Solution()
nums1 = [0,0,0,0,0]
nums2 = [0,0,0,0,0]
print(sol.findLength(nums1,nums2))
                 
# Second solution
class Solution(object):

    def findLength(self, nums1, nums2):
        # Creating a 2D array 
        dp = [[0]*(len(nums1)+1) for _ in range(len(nums2)+1)]
        max_len = float("-inf")

        for row in range(1,len(nums1) +1):
            for column in range(1,len(nums2)+1):

                # If the value of the row and the column are the same
                if nums1[row-1]== nums2[column-1]:

                    # We take the top left value and add 1
                    dp[row][column] = dp[row-1][column-1] + 1

                    # The greatest value in the 2D array will be the max len
                    # So we compare max len with each iteration
                    max_len = max(max_len,dp[row][column])
                
                    # If the value of the row and the column are different, it stays 0
                    
        return 0 if max_len==float("-inf") else max_len

sol = Solution()
nums1 = [3,2,1,2,1]
nums2 = [7,6,3,2,1]
print(sol.findLength(nums1,nums2))