
# Python program to demonstrate search operation in binary search tree 

# A utility class that represents an individual node in a BST 
class Node: 
	def __init__(self,key): 
		self.left = None
		self.right = None
		self.val = key 

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

#  function to search a given key in BST 
def search(root,key): 
	
	# Base Cases: root is null or key is present at root 
	if root is None or root.val == key: 
		return root.val

	# Key is greater than root's key 
	if root.val < key: 
		return search(root.right,key) 
	
	# Key is smaller than root's key 
	return search(root.left,key) 



#
root = Node(60) 
insert(root,Node(30)) 
insert(root,Node(20)) 
insert(root,Node(40)) 
insert(root,Node(70)) 
insert(root,Node(50)) 
insert(root,Node(80)) 


valueToSearch = int(input("enter the value to search: "))

print(f"{search(root,valueToSearch)} is found")