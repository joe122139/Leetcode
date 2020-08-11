#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import List

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists)==0:
            return None

        heap = []
        from heapq import heappop,heappush
        result= ListNode(None)
        p_re = result
        for l in lists:
            while(l):
                heappush(heap,l.val)
                l = l.next
        
        for i in range(0,len(heap)):
            popped = ListNode(heappop(heap))
            print(popped)
            p_re.next = popped
            p_re = p_re.next

        return result.next


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    ary = [[1,4,5],[1,3,4],[2,6]]
    #ary = ["i", "love", "leetcode", "i", "love", "coding","love","love","luca","wang"]
    #ary = [1,3]
    print(s.mergeKLists(ary))

