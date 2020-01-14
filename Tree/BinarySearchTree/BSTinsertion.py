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

# A utility function to do inorder tree traversal 
def inorder(root): 
	if root: 
		inorder(root.left) 
		print(root.val,end=" ") 
		inorder(root.right) 




rootval = int(input("Enter root of BST: ")) 
root=Node(rootval)
choice = None
while(choice!=3):
    print()
    print('###### Binary Tree operations ######')
    print('1. insert integer to Binary Search Tree')
    print('2. inorder traversal')
    print('3. Exit')

    choice = input("Enter your choice: ")
    choice = int(choice)

    if choice == 1:
        valueToInsert = int(input("Enter a number to insert: ")) 
        insert(root,Node(valueToInsert))

    elif choice == 2:
        # Print inoder traversal of the BST 
        print("Inorder traversal of the Binary Search Tree is:", end=" ")
        inorder(root)
    elif choice == 3:
        print("program exited")
        break
            
    else:
        print("Invalid Choice")



