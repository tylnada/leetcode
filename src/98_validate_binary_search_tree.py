  #recursion  
  def isValidBST(self, root, floor=float('-inf'), ceiling=float('inf')):
        if not root:
            return True
        if root.val >= ceiling or root.val <= floor:
            return False
        # in the left branch, root is the new ceiling; contrarily root is the new floor in right branch
        return(self.isValidBST(root.left, floor, min(root.val, ceiling)) and self.isValidBST(root.right,max(root.val, floor), ceiling))
