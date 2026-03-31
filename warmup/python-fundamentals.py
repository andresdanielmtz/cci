from collections import deque

# stacks 

stack = []

stack.append(1)
stack.append(2)

topElement = stack[-1]
print(topElement) # 2 

poppedElement = stack.pop()
print(poppedElement) # 2 

print(stack) # 1

isEmpty = not bool(stack)
print("isEmpty", isEmpty)

size = len(stack)
print("size", size)

stack_deque = deque()
for i in range(10):
    stack_deque.append(i)
print("stack deque", stack_deque)
print("stack pop", stack_deque.pop()) # 9 is removed
print("stack top", stack_deque[-1]) # so 8 is now the top
print("stack popleft", stack_deque.popleft()) # 0

# combinations 

lst_1 = [1,2,3]
lst_2 = [3,1,4]
comb = [(x,y) for x in lst_1 for y in lst_2 if x != y]
print("comb", comb)

# dictionary

tel = {'jack': 4098, 'sape': 4139}
