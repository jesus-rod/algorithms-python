import stack as s


# Recursive function that inserts an element at the bottom of a stack.
def insertAtBottom(stack, item):
    # Base case
    if s.isEmpty(stack):
        s.push(stack, item)

    # Recursive case
    else:
        temp = s.pop(stack)
        insertAtBottom(stack, item)
        s.push(stack, temp)


def reverse(stack):
    # Recursive case
    if not s.isEmpty(stack):
        temp = s.pop(stack)
        reverse(stack)
        print("appending", temp)
        stack.append(temp)


# Driver Code
myStack = s.createStack()
s.push(myStack, str(8))
s.push(myStack, str(5))
s.push(myStack, str(3))
s.push(myStack, str(2))

print("Original Stack")
s.printStack(myStack)

reverse(myStack)

print("\n\nReversed Stack")
s.printStack(myStack)
