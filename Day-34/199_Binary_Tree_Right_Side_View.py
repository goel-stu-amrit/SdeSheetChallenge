class Solution(object):
    def rightSideView(self, root):
        if not root: return []
        leveltree = [[root]]
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if len(leveltree) <= level+1:
                leveltree.append([])
            if node.left:
                queue.append((node.left, level+1))
                leveltree[level+1].append(node.left)
            if node.right:
                queue.append((node.right, level+1))
                leveltree[level+1].append(node.right)
        res = []
        for i in leveltree[:-1]:
            res.append(i[-1].val)
        return res