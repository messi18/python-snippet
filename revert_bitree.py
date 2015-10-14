def revert_bitree(root_node):
  stack=[]
  stack.append(root_node)
  while len(stack) > 0:
    node=stack.pop()
    if isinstance(node,Node):
      stack.append(node.left)
      stack.append(node.right)
      node.left,node.right=node.right,node.left
    
class Node:
  def __init__(self,left,right):
    self.left = left
    self.right = right
  def __str__(self):
    return "(%s,%s)" % (self.left,self.right)
if __name__ == "__main__":
  bitree=Node(Node(1,2),Node(3,Node(4,5)))
  revert_bitree(bitree)
  print bitree
