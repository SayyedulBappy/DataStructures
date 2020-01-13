
from Queue import Queue


# create queue

queue = Queue()

choice = None
while(choice!=6):
    print()
    print('###### queue operations ######')
    print('1. Display the integers')
    print('2. Enqueue integers to queue')
    print('3. Deque integers from queue')
    print('4. Front of queue')
    print('5. Rear of queue')
    print('6. Exit')

    choice = input("Enter your choice: ")
    choice = int(choice)

    if choice == 1:
        for item in queue.items:
            print(item,end=" ")
        
    elif choice == 2:
        # push elements
        itemToAdd = input("Enter integer to enqueue: ")
        queue.enqueue(itemToAdd)
        
    elif choice == 3:
        # remove element
        print(queue.dequeue())
    elif choice == 4:
        #  element at front
        print(f"Front of queue is {queue.front()}")
    elif choice == 5:
        # element at rear
        print(f"Rear of queue is {queue.rear()}")
    elif choice == 6:
        print("program exited")
        break
    else:
        print("Invalid Choice")





