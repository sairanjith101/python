from collections import deque

char = deque([1,2,3])

char.append(4)
print(char)

char.appendleft(6)
print(char)

char.pop()
print(char)

char.popleft()
print(char)