class Solution(object):
    def widthOfBinaryTree(self, root):
        if not root: return 0
        ans, start = 0, 0
        queue = [(root, 0)]
        while start < len(queue):
            size = len(queue) - start
            mmin = queue[start][1]
            first, last=0, 0
            for i in range(size):
                node, idx= queue[start + i]
                currId= idx-mmin
                if i==0: first =currId
                if i == size-1: last=currId
                if node.left: queue.append((node.left, currId*2+1))
                if node.right: queue.append((node.right, currId*2+2))
            ans = max(ans, last - first + 1)
            start += size
        return ans