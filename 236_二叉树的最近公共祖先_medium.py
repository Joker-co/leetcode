# 递归
def moni(node, p, q):
    if not node or node==p or node==q:
        return node
    left = moni(node.left, p, q)
    right = moni(node.right, p, q)
    if not left and not right:
        return None
    if not left:
        return right
    if not right:
        return left
    return node

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = moni(root, p, q)
        return node
        
 # 非递归
 class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root==q or root==p:
            return root
        dic_node = {}
        dic_node[root] = None
        stack = [root]
        while p not in dic_node or q not in dic_node:
            parent = stack.pop()
            if parent.left:
                dic_node[parent.left] = parent
                stack.append(parent.left)
            if parent.right:
                dic_node[parent.right] = parent
                stack.append(parent.right)
        path = []
        p_tmp = p
        while p_tmp:
            path.append(p_tmp)
            p_tmp = dic_node[p_tmp]
        q_tmp = q
        while q_tmp not in path:
            q_tmp = dic_node[q_tmp]
        return q_tmp
