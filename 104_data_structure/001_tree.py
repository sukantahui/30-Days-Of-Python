from bigtree import Node, print_tree

a = Node("a", age=90)
b = Node("b", age=65, parent=a)
c = Node("c", age=60, parent=a)

a.children
# (Node(/a/b, age=65), Node(/a/c, age=60))

a.depth, b.depth
# (1, 2)

a.max_depth
# 2

print_tree(a, attr_list=["age"])