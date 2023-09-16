from binarytree import bst
def print_traversal(list,order_type=""):
    print("\n\n",order_type,":")
    for i in range(len(list)):
        print(list[i].value,end=",")
    print()    
  
# # Create a random BST 
# # of any height
# root = bst()
# print('BST of any height : \n',
#       root)
  
# # Create a random BST of 
# # given height
# root2 = bst(height = 2)
# print('BST of given height : \n',
#       root2)
  
# Create a random perfect 
# BST of given height
root3 = bst(height = 4, is_perfect = False)
tree_list = root3.values
res = list(filter(lambda item: item is not None, tree_list))
print(res)
print('Perfect BST of given height : \n',root3)
print_traversal(root3.preorder,"Preorder")
print_traversal(root3.inorder,"inorder")
print_traversal(root3.postorder,"postorder")
