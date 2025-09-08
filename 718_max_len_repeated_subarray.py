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
                 
                
