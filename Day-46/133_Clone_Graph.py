class Solution(object):
    def cloneGraph(self, node):
        if not node: return 
        obj = {node: Node(node.val)}
        queue = deque([node])
        while queue:
            curr = queue.popleft()
            for nei in curr.neighbors:
                if nei not in obj:
                    obj[nei] = Node(nei.val)
                    queue.append(nei)
                obj[curr].neighbors.append(obj[nei])

        return obj[node]
