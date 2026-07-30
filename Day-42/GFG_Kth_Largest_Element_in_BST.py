class Solution:
    def kthLargest(self, root, k):
        self.count = 0
        self.ans = None

        def reverseInorder(node):
            if not node or self.ans is not None:
                return

            reverseInorder(node.right)

            self.count += 1
            if self.count == k:
                self.ans = node.data
                return

            reverseInorder(node.left)

        reverseInorder(root)
        return self.ans
        