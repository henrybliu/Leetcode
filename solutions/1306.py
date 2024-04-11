from collections import deque


class Solution:
    """
    Do BFS from the start and visit other nodes that can be reached and test if
    these nodes are the value 0. Make sure to not revisit nodes.

    Time: O(n)
    Space: O(n)
    """

    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        visited = set()

        while q:
            curr = q.popleft()

            if arr[curr] == 0:
                return True

            visited.add(curr)

            left = curr - arr[curr]
            right = curr + arr[curr]

            if left >= 0 and left not in visited:
                q.append(left)
            if right < len(arr) and right not in visited:
                q.append(right)

        return False
