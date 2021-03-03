
'''Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor.

The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.

Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.
'''



class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        uni = 0
        for i in range(len(candyType)):
            for j in range(0,i):
                if candyType[i] == candyType[j]:
                    break 
            else:
                uni += 1 
        return min(uni,len(candyType)//2)
