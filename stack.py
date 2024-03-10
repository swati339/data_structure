stack = []
def push():
    element = ("enter the element")
    stack.append(element)
    print(stack)

def pop_element():
    if not stack: 
        print("stack is empty")
    else:
        e = stack.pop()
        print("element removed", e)
        print(stack)

while True:
    print("Enter the operation: \n1. Push\n2. Pop element\n3. Exit")
    choice = int(input())
    
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Enter the correct operation")
    