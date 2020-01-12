

from collections import deque ## for quicker operations
# create queue

print("Enter integers separated by spaces to create an queue: ", end=" ")

queue = deque(map(int,input().strip().split()))

# display the created queue

for item in queue:
    print(item,end=" ")

choice = None
while(choice!=4):
    print()
    print('###### queue operations ######')
    print('1. Display the integers')
    print('2. Enqueue integers to queue')
    print('3. Deque integers from queue')
    print('4. Exit')

    choice = input("Enter your choice: ")
    choice = int(choice)

    if choice == 1:
        for item in queue:
            print(item,end=" ")
        
    elif choice == 2:
        # push elements
        itemToAdd = input("Enter integer to push: ")
        queue.append(itemToAdd)
        
    elif choice == 3:
        # remove element
        print(queue.popleft())

    elif choice == 4:
        print("program exited")
        break
    else:
        print("Invalid Choice")





