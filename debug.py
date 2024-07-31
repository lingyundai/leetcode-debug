# from typing import Optional

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
#         def dfs(node, cur):
#             if not node:
#                 return False
            
#             cur += node.val

#             if not node.left and not node.right:
#                 return cur == targetSum

#             return (dfs(node.left, cur) or dfs(node.right, cur))


#         return dfs(root, 0)

# root = TreeNode(5)
# root.left = TreeNode(4)
# root.right = TreeNode(8)
# root.left.left = TreeNode(11)
# root.left.left.left = TreeNode(7)
# root.left.left.right = TreeNode(2)
# root.right.left = TreeNode(13)
# root.right.right = TreeNode(4)
# root.right.right.right = TreeNode(1)

# solution = Solution()
# solution.hasPathSum(root, 22)

# def dfs(node, target, adjList, visit):
#     if node in visit:
#         return 0
#     if node == target:
#         return 1
    
#     count = 0
#     visit.add(node)
#     for neighbor in adjList[node]:
#         count += dfs(neighbor, target, adjList, visit)
#     visit.remove(node)

#     return count

# dfs("A", "E", { "A": ["B"], "B": ["C", "E"], "C": ["E"], "E": ["D"], "D": [] }, set())

# # Shortest path from node to target
# from collections import deque
# def bfs(node, target, adjList):
#     length = 0
#     visit = set()
#     visit.add(node)
#     queue = deque()
#     queue.append(node)

#     while queue:
#         for i in range(len(queue)):
#             curr = queue.popleft()
#             if curr == target:
#                 return length

#             for neighbor in adjList[curr]:
#                 if neighbor not in visit:
#                     visit.add(neighbor)
#                     queue.append(neighbor)
#         length += 1
#     return length
# bfs("A", "E", { "A": ["B"], "B": ["C", "E"], "C": ["E"], "E": ["D"], "D": [] })

# # Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

# from typing import Optional

# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         oldToNew = {}

#         def dfs(node):
#             if node in oldToNew:
#                 return oldToNew[node]
            
#             copy = Node(node.val)
#             oldToNew[node] = copy

#             for ne in node.neighbors:
#                 copy.neighbors.append(dfs(ne))
#             return copy
        
#         return dfs(node) if node else None

# # Create the graph using the adjacency list [[2, 4], [1, 3], [2, 4], [1, 3]]
# adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]

# # Create nodes
# nodes = [Node(i+1) for i in range(len(adjList))]

# # Populate neighbors
# for i, neighbors in enumerate(adjList):
#     for neighbor in neighbors:
#         nodes[i].neighbors.append(nodes[neighbor - 1])

# # Clone the graph
# solution = Solution()
# solution.cloneGraph(nodes[0])