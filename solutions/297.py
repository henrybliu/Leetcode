# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Codec:
    """
    Serialize by performing a level-order traversal, adding a comma between
    each node and N for a null node. This will create the encrypted string.

    Deserialize by reading from the encrypted string. Use a queue to keep
    track of the nodes that we haven't completed. Use an index pointing to the
    encrypted string to indicate what we have/not yet added. We first add the
    children nodes of the node being created before moving onto the next node.

    Time: O(n) for both
    Space: O(n) for both
    """

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "N"

        encrypt = []
        q = deque()
        q.append(root)

        while q:
            curr = q.popleft()

            if curr:
                encrypt.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)

            else:
                encrypt.append("N")

        toString = ",".join(encrypt)
        return toString

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")

        if data[0] == "N":
            return None

        root = TreeNode(data[0])
        q = deque([root])
        i = 1

        while q:
            curr = q.popleft()

            if curr:
                if i < len(data) and data[i] != "N":
                    curr.left = TreeNode(data[i])
                    q.append(curr.left)

                i += 1

                if i < len(data) and data[i] != "N":
                    curr.right = TreeNode(data[i])
                    q.append(curr.right)

                i += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
