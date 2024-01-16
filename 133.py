class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def cloneGraph(self, node):
        visit_node={}
        def clone_node(node, visit_node):
            if node in visit_node:
                new_node= visit_node[node]
                return new_node
            else:
                new_node=Node(node.val)
                visit_node[node]=new_node
            for i in node.neighbors:
                new_node.neighbors.append(clone_node(i, visit_node))
            
            return new_node
        new=clone_node(node, visit_node)
        return new

        
