# A single node of a singly linked list
class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # insertion method for the linked list
  def insertAtEnd(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode

  def insertAtBegining(self,data):
        newNode = Node(data)
        # Update the new nodes next val to existing node
        newNode.next = self.head
        self.head = newNode

  def insertInbetween(self,middle_node,data):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        newNode = Node(data)
        newNode.next = middle_node.next
        middle_node.next = newNode

  def RemoveNode(self, Removekey):

        headval = self.head

        if (headval is not None):
            if (headval.data == Removekey):
                self.head = headval.next
                headval = None
                return

        while (headval is not None):
            if (headval.data == Removekey):
                break
            prev = headval
            headval = headval.next

        if (headval == None):
            return

        prev.next = headval.next

        headval = None

  # print method for the linked list
  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next
