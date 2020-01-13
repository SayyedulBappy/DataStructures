

from SinglyLinkedList import LinkedList

# create Linked List

LL = LinkedList()

choice = None
while(choice!=5):
    print('###### Singly Linked List operations ######')
    print('1. Display the integers')
    print('2. insert integer at end of Linked List')
    print('3. insert integer at begining of Linked List')
    print('4. remove integer from Linked List')
    print('5. Exit')

    choice = input("Enter your choice: ")
    choice = int(choice)

    if choice == 1:
        LL.printLL()
    elif choice == 2:
        
        itemToAdd = input("Enter integer to push: ")
        LL.insertAtEnd(itemToAdd)
    elif choice == 3:
        
        itemToAdd = input("Enter integer to push: ")
        LL.insertAtBegining(itemToAdd)
    elif choice == 4:
        itemToRemove = input("Enter integer to Remove: ")
        LL.RemoveNode(itemToRemove)

    elif choice == 5:
        print("program exited")
        break
    else:
        print("Invalid Choice")

