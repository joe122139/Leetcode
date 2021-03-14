#
# @lc app=leetcode.cn id=692 lang=python3
#
# [692] 前K个高频单词
#

# @lc code=start
from heapq import heappop,heappush
from collections import Counter
from typing import List

class FreqWord(object):
    def __init__(self,freq,word):
        self.word = word
        self.freq = freq
    
    def __lt__(self,other):
        if self.freq != other.freq:
            return self.freq < other.freq  # self.freq<other.freq
        else:
            return other.word< self.word  # other.word < self.word
#            return self.wordother.word  # other.word < self.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #use hash for each word to calculate the freq.
        counter = Counter(words)
        
        print(counter)
        #use the heap to store the word and freq.
        h=list()
        for key,cnt in counter.items():
            heappush(h,FreqWord(cnt,key))
            if len(h)>k:
                heappop(h)

   #     result=[]

   #     print('h',h)
   #     for i in range(0,len(h)):
   #         popped=heappop(h)
   #         print(popped.word)
   #         result.append(popped.word)

        return [heappop(h).word for _ in range(k)][::-1]
        #return result[::-1]
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    #ary = [4,5,6,7,0,1,2,3]
    ary = ["i", "love", "leetcode", "i", "love", "coding","love","love","luca","wang"]
    #ary = [1,3]
    print(s.topKFrequent(ary,4))
