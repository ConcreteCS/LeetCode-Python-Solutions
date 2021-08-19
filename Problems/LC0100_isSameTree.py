# isSameTree3:
# Time:  O(n)
# Space: O(n)
#
# Given the roots of two binary trees p and q, write a function to check if they 
# are the same or not. Two binary trees are considered the same if they are structurally
# identical, and the nodes have the same value.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree1(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree1(p.left, q.left) and self.isSameTree1(p.right, q.right)
        else:
            return p == q
    
    # DFS with stack
    def isSameTree2(self, p, q):
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            elif None in [node1, node2]:
                return False
            else:
                if node1.val != node2.val:
                    return False
                stack.append((node1.right, node2.right))
                stack.append((node1.left, node2.left))
        return True
    
    # BFS with queue
    def isSameTree3(self, p, q):
        import collections
        queue = collections.deque([(p, q)])
        while queue:
            node1, node2 = queue.popleft()
            if not node1 and not node2:
                continue
            elif None in [node1, node2]:
                return False
            else:
                if node1.val != node2.val:
                    return False
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))
        return True

#     2
#    / \
#   1   3
#  / \
# 4   5
t1 = TreeNode(2)
t1.left = TreeNode(1)
t1.right = TreeNode(3)
t1.left.left = TreeNode(4)
t1.left.right = TreeNode(5)
#     2
#    / \
#   1   3
#  / \
# 4   5
t2 = TreeNode(2)
t2.left = TreeNode(1)
t2.right = TreeNode(3)
t2.left.left = TreeNode(4)
t2.left.right = TreeNode(5)
#     2
#    / 
#   1   
#  / \
# 4   5
t3 = TreeNode(2)
t3.left = TreeNode(1)
t3.left.left = TreeNode(4)
t3.left.right = TreeNode(5)

print(Solution().isSameTree1(t1, t2))
print(Solution().isSameTree2(t1, t2))
print(Solution().isSameTree3(t1, t2))
print(Solution().isSameTree1(t1, t3))
print(Solution().isSameTree2(t1, t3))
print(Solution().isSameTree3(t1, t3))
