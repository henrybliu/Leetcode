class Solution:
    """
    We want to satisfy as many children as possible. This can be greedily
    accomplished by trying to satisfy the children that require the least
    amount of cookies first and by giving them the minimum cookie size
    necessary. This can be done so by sorting both the children's requirements
    and the cookie sizes. If we can satisfy a child's cookie desires, we give
    them that cookie, otherwise, we move on to the next largest cookie.

    Time: O(nlogn)
    Space: O(1)
    """

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        gIdx = 0
        sIdx = 0
        content = 0

        while gIdx < len(g) and sIdx < len(s):
            if s[sIdx] >= g[gIdx]:
                content += 1
                sIdx += 1
                gIdx += 1
            else:
                sIdx += 1

        return content
