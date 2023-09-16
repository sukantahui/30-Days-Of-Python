from binarytree import tree
from binarytree import build
import random
def print_traversal(list):
    print()
    for i in range(len(list)):
        print(list[i].value,end=",")
    print()    
# my_tree = tree(height=3, is_perfect=False, letters=True)

# print(my_tree)
# print(my_tree.inorder)


# list_length = [7, 3, 2, 6, 9, 1, 5, 8]
list_length = random.randint(8,12)
randomlist = random.sample(range(10, 50),list_length )
root = build(randomlist)
print(root)
print(root.values)
# print("\nInorder")
# print(root.inorder)
# print("\nPreorder")
# print(root.preorder)
# print("\nPostorder")
# print(root.postorder)


print(print_traversal(root.preorder))
print(print_traversal(root.inorder))
print(print_traversal(root.postorder))


print(randomlist)



