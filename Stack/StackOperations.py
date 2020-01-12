
# create Stack

print("Enter integers separated by spaces to create an stack: ", end=" ")

stack = list(map(int,input().strip().split()))

# display the created stack

for item in stack:
    print(item,end=" ")
print()
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
        for item in stack:
            print(item,end=" ")
        
    elif choice == 2:
        # push elements
        itemToAdd = input("Enter integer to push: ")
        stack.append(itemToAdd)
        
    elif choice == 3:
        # pop element
        print(stack.pop())
    elif choice == 4:
        top = stack[-1]
        print(f"Top of stack is {top}")
    elif choice == 5:
        print("program exited")
        break
    else:
        print("Invalid Choice")





