
# create array

print("Enter integers separated by spaces to create an array: ", end=" ")

arr = list(map(int, input().split()))

# display the created array

for item in arr:
    print(item,end=" ")

choice = None
while(choice!=4):
    print('###### Array operations ######')
    print('1. display the items')
    print('2. insert integer to array')
    print('3. remove integer from array')
    print('4. Exit')

    choice = input("Enter your choice: ")
    choice = int(choice)

    if choice == 1:
        for item in arr:
            print(item,end=" ")
        
    elif choice == 2:
        # insert elements
        itemToAdd = int(input("Enter integer to insert: "))
        insertPosition = int(input("Enter position to insert: "))
        arr.insert(insertPosition,itemToAdd)
        
    elif choice == 3:
        # remove element
        itemToRemove = int(input("Enter integer to remove: "))
        index = arr.index(itemToRemove)
        print(arr.pop(index))

    elif choice == 4:
        print("program exited")
        break
    else:
        print("Invalid Choice")





