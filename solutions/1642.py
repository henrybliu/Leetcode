import heapq

class Solution:
    '''
    Idea is that we can retroactively decide to use a ladder on a previous
    # building. So when we run out of bricks, we should have used a ladder
    before instead. We want to use the ladder on the greatest height
    difference. Use a max heap to keep track of the largest height that we
    have encountered so far. So that if we don't have enough bricks, we can use
    a ladder at a previous location and use bricks instead.

    Time: O(nlogn)
    Space: O(n)
    '''
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # max heap to keep track of largest heights that we have seen so far
        # and to use a ladder there instead
        h = []

        for b in range(len(heights)-1):
            heightDiff = heights[b+1]-heights[b]

            # we are able to move on to the next building without bricks/ladders
            if heightDiff <= 0:
                continue
            
            # we need to use bricks/ladders
            bricks -= heightDiff
            heapq.heappush(h, -heightDiff)

            # we ran out of bricks, so want to try using a ladder on some
            # previous (including the current one) building instead
            if bricks < 0:
                if ladders:
                    ladders-=1
                    bricks += -heapq.heappop(h)
                else:
                    return b

        # was able to reach all of the buildings
        return len(heights)-1