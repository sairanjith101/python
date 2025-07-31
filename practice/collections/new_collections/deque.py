from collections import deque

char = deque([1,2,3])
print(char)

#enqueue
char.append(4)
print(char)


char.appendleft(6)
print(char)

#peek
char.pop()
print(char)

#dequeue 
char.popleft()
print(char)

#note
# enqueue adds an element to the end of the queue.
# dequeue removes an element from the front.
# peek shows the front element without removing it