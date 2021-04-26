'''
You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.
'''

#SOLUTION:
class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        jumps_pq = []
        for i in range(len(heights) - 1):
            jump_height = heights[i + 1] - heights[i]
            if jump_height <= 0: continue
            heappush(jumps_pq, jump_height)
            if len(jumps_pq) > ladders:
                bricks -= heappop(jumps_pq)
            if(bricks < 0) : return i
        return len(heights) - 1
