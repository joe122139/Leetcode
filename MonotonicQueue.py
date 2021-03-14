class MonotonicQueue(object):
    def __init__(self):
        self.__data =[]

    def push(self,e,nums):
        size = len(self.__data)
        while size > 0 and nums[e] >= nums[self.__data[size-1]]:
            self.__data.pop(size-1)
            size-=1
        self.__data.append(e)

    def pop(self):
        popped = self.__data.pop(0)
        return popped
    
    def max(self):
        return self.__data[0]
    
    def print(self,nums):
        for i in self.__data:
            print(nums[i], end=' ') 
        print()

if __name__ == "__main__":
    h = MonotonicQueue()
    h.push(1)
    h.push(2)
    h.push(3)
    h.push(2)
    print(h.pop())
    print(h.pop())
