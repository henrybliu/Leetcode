# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Use a pointer to keep track of the current node in the linked list.
    Otherwise, traversing the matrix in a spiral pattern is very similar to the
    regular spiral matrix problem.
    """

    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1 for _ in range(n)] for _ in range(m)]

        curr = head
        t, l = 0, 0
        b, r = m - 1, n - 1

        while curr:
            # top row
            for i in range(l, r + 1):
                if curr:
                    res[t][i] = curr.val
                    curr = curr.next
                else:
                    break
            t += 1

            # right column
            for i in range(t, b + 1):
                if curr:
                    res[i][r] = curr.val
                    curr = curr.next
                else:
                    break

            r -= 1

            # bottom row
            for i in range(r, l - 1, -1):
                if curr:
                    res[b][i] = curr.val
                    curr = curr.next
                else:
                    break
            b -= 1

            # left column
            for i in range(b, t - 1, -1):
                if curr:
                    print(i, l)
                    res[i][l] = curr.val
                    curr = curr.next
                else:
                    break

            l += 1

        return res
