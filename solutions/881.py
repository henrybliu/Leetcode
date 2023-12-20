class Solution:
    '''
    Would be very easy to sort the array of people. Want to put the heaviest
    and smallest people in the same boat.

    Time: O(nlogn)
    Space: O(1)
    '''
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0

        l = 0
        r = len(people)-1

        while l<=r:
            add = people[l]+people[r]
            if add > limit:
                r-=1
                boats +=1
            else:
                boats +=1
                r-=1
                l+=1

        return boats