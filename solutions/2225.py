from collections import defaultdict


class Solution:
    """
    Maintain a hashmap of each player and their number of losses. Then,
    categorize each player into the two arrays: if the didn't lose or if they
    only lost one match. Make sure to sort both of these arrays since the two
    lists should be returned in sorted order.

    Time: O(nlogn)
    Space: O(n)
    """

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        played = set()
        numLosses = defaultdict(int)

        for w, l in matches:
            played.add(w)
            played.add(l)

            numLosses[l] += 1

        noLosses = []
        lostOne = []

        for player in played:
            if numLosses[player] == 1:
                lostOne.append(player)
            elif numLosses[player] == 0:
                noLosses.append(player)

        noLosses.sort()
        lostOne.sort()

        return [noLosses, lostOne]
