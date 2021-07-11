'''The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
'''
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small, self.large = [],[]
        

    def addNum(self, num: int) -> None:
        heappush(self.small, -num)           
        heappush(self.large, -heappop(self.small))
        
        if len(self.small) < len(self.large):
            heappush(self.small, -heappop(self.large))

    def findMedian(self) -> float:
        if len(self.large) != len(self.small):
            return -self.small[0]                  
        else:
            return (self.large[0] - self.small[0]) / 2 
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
