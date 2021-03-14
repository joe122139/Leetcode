#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if(len(strs)==0):
            return strs

        dict = {}
        for s in (strs):
            sort_str = "".join(sorted(s))
            wordList=[]
            if sort_str in dict:
                dict[sort_str].append(s)
            else:
                dict[sort_str] = [s]

        return list(dict.values())

# @lc code=end
if __name__ == "__main__":
    s = Solution()
    ary = ["eat","tea","tan","ate","nat","bat"]
    print(s.groupAnagrams(ary))


