# Python program to demonstrate insert operation in binary search tree 

# A utility class that represents an individual node in a BST 
class Node: 
	def __init__(self,key): 
		self.left = None
		self.right = None
		self.val = key 

# A utility function to insert a new node with the given key 
def insert(root,node): 
	if root is None: 
		root = node 
	else: 
		if root.val < node.val: 
			if root.right is None: 
				root.right = node 
			else: 
				insert(root.right, node) 
		else: 
			if root.left is None: 
				root.left = node 
			else: 
				insert(root.left, node) 

# function to do inorder tree traversal 
def inorder(root): 
	if root: 
		inorder(root.left) 
		print(root.val,end=" ") 
		inorder(root.right) 

# BST creation

root = Node(60) 
insert(root,Node(30)) 
insert(root,Node(20)) 
insert(root,Node(40)) 
insert(root,Node(70)) 
insert(root,Node(50)) 
insert(root,Node(80)) 

# Print inoder traversal of the BST 
print("Inorder traversal of the Binary Search Tree is:", end=" ")
inorder(root) 

