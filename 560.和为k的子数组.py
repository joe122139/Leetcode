#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#

# @lc code=start
from typing import List
class Solution:
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        s = 0
        pre_sum = {}
        minus_k = []
        for i in range(0, len(nums)):
            s += nums[i] 
            print(s)
            pre_sum[s] = i
            minus_k.append(s - k)
        
        cnt =0
        for idx in range(len(minus_k)):
            if idx==0:
                cnt = (1 if minus_k[idx]==k else 0)
            elif minus_k[idx] in pre_sum.keys():
                cnt+=1
            if minus_k[i] == 0:
                cnt+=1

        return cnt
        '''

    def subarraySum(self, nums: List[int], k: int) -> int:
        Hash = {0: 1}
        numSum = 0
        res = 0
        for i in range(len(nums)):
            numSum += nums[i]
            res += Hash.get(numSum-k, 0)
            Hash[numSum] = Hash.get(numSum, 0)+1
            print(numSum,res,Hash[numSum])
        
        return res


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    #ary = [3,5,10,-2,6,1]
    #ary = [1]
    ary = [-1,-1,1,2]
#    ary = [3,5,10,-2,6,1,3,1,3,1,-5,0,0,4,-8]
    print(s.subarraySum(ary,0))


