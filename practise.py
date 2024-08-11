''''
how to check if a string is a palidrome

'''

def findPalindrome():
    name = "racecar"
    print(name)
    length = len(name)
    list1 = []
    list2 = []
    for i in range(0,length):
        list1.append(name[i])

    for i in range(length-1,-1,-1):
        # print (f"reverse {name[i]}"
        list2.append(name[i])

    print(list1)
    print(list2)
    if list1 == list2:
        print (f"String is a palidrome {name}")
    else:
        print(f"String is not  palidrome {name}")


''''
how to add numbers between two loc in a list 
'''

def find_largest_numbers():
    '''
    Find the three largest elements in an array
    '''
    my_list = [10,11, 8, 9, 20, 50, 70, 37]
    sorted1 = sorted(my_list,reverse=False)  # Sort the list in descending order
    print(sorted1)
    largest_three = sorted1[:3]  # Take the first three elements
    print("The three largest numbers are:", largest_three)

''''
how to add numbers between two loc in a list 
'''
def removeduplicate():
    my_list = [1,9,3,9,5,6]
    sorted_set = set(my_list)
    print(sorted_set)
    print(list(sorted_set))


def operationinlist(start_index,end_index,operation):
    list = []
    for i in range (1,10,1):
        # print(i)
        list.append(i)
    print (list)
    if operation == "add":
        value = 0
    elif operation == "multiply":
        value = 1
    else:
        print("nothing work in progress")
    for i in range(start_index,end_index+1):
        if operation == "add":
            value += list[i]
        elif operation == "multiply":
            value *= list[i]
        else:
            print ("nothing work in progress")
    print(value)
if __name__ == "__main__":
    #findPalindrome()
    #operationinlist(1,4,"multiply")
    #operationinlist(1,4,"add")
    #find_largest_numbers()
    removeduplicate()