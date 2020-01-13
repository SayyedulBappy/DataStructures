
from Array import Array 
# create array

arr = Array()

# display the created array

choice = None
while(choice!=4):
    print('###### Array operations ######')
    print('1. display item')
    print('2. append item')
    print('3. insert item at a specific position')
    print('4. pop item')
    print('5. remove item at first occurrance')
    print('6. index of item at first occurrance')
    print('7. reverse array')
    print('8. Exit')

    choice = input("Enter your choice: ")
    choice = int(choice)

    if choice == 1:
        for item in arr.items:
            print(item,end=" ")
        
    elif choice == 2:
        # append elements
        itemToAdd = int(input("Enter integer to append: "))
        arr.append(itemToAdd)
        
    elif choice == 3:
        # insert elements
        itemToInsert = int(input("Enter integer to insert: "))
        insertPosition = int(input("Enter position to insert: "))
        arr.insert(insertPosition,itemToInsert)
        
    elif choice == 4:
        # pop element
        print(f"popped item is {arr.pop()}")
    elif choice == 5:
        # remove element
        itemToRemove = int(input("Enter integer to remove: "))
        print(arr.remove(itemToRemove))
    elif choice == 6:
        # index element
        item = int(input("Enter integer to find index: "))
        print(arr.index(item))
    elif choice == 7:
        # reverse array
        arr.reverse()
    elif choice == 8:
        print("program exited")
        break
    else:
        print("Invalid Choice")





