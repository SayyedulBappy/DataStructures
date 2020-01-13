from stack import Stack

# create Stack

stack = Stack()

choice = None
while(choice!=5):
    print('###### Stack operations ######')
    print('1. Display the integers')
    print('2. Push integers to stack')
    print('3. Pop integers from stack')
    print('4. Top of stack')
    print('5. Exit')

    choice = input("Enter your choice: ")
    choice = int(choice)

    if choice == 1:
        for item in stack.items:
            print(item,end=" ")
        
    elif choice == 2:
        # push elements
        itemToAdd = input("Enter integer to push: ")
        stack.push(itemToAdd)
        
    elif choice == 3:
        if stack.is_empty():
            print("Stack is empty")
        # pop element
        print(stack.pop())
    elif choice == 4:
        top = stack.items[-1]
        print(f"Top of stack is {top}")
    elif choice == 5:
        print("program exited")
        break
    else:
        print("Invalid Choice")





