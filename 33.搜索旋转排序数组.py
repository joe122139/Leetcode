# @before-stub-for-debug-begin
#from python3problem33 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def findPivot(self,nums,le,ri):
        while(le < ri -1):
            pi = int((le+ri)/2)
            #pivot on the right
            if(nums[pi] > nums[ri]):
                le = pi 
            else:
                ri = pi 
        if nums[le]>nums[ri]:
            return le
        else:
            return ri

    def binSearch(self, nums,le, ri, target):
        while le <= ri:
            pi = le + int((ri - le)/2)
            #pivot on the right
            if(nums[pi] > target):
                ri = pi-1
            elif nums[pi]<target:
                le = pi+1
            else:
                return pi
        # If we reach here, then the element was not present 
        return -1

    def search(self, nums: List[int], target: int) -> int:
        #find the pivot
        if len(nums)==0:
            return -1
        elif len(nums)==1:
            return 0 if target == nums[0] else -1
        
        le = 0
        size = len(nums)
        ri = size -1
        pivot = self.findPivot(nums,le, ri)
        print(pivot)

        # check which side the target is 
        if pivot!=ri and nums[pivot+1]<=target<=nums[ri]:
            le = pivot+1
        else:
            ri = pivot

        # do regular binarySearch
        return self.binSearch(nums,le,ri,target)

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    ary = [4,5,6,7,0,1,2,3]
    ary = [1,3]
    #print(s.findPivot(ary,0,len(ary)-1))
    print(s.search(ary,0))
