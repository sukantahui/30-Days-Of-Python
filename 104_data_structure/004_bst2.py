class bst:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
def insert(root, key):
    if not root:
        return bst(key)
    if key >= root.value:
        root.right = insert(root.right, key)
    elif key < root.value:
        root.left = insert(root.left, key)
    return root

def insert_values(root, values):
    for value in values:
        root = insert(root, value)
    return root

def print2DTree(root, space=0, LEVEL_SPACE = 5):
    if (root == None): return
    space += LEVEL_SPACE
    print2DTree(root.right, space)
    # print() # neighbor space
    for i in range(LEVEL_SPACE, space): print(end = " ")  
    print("|" + str(root.value) + "|<")
    print2DTree(root.left, space)

root = insert_values(None, [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])
print2DTree(root) 