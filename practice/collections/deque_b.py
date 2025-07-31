from collections import deque

# Initialize a queue with some elements
char = deque([1, 2, 3])
print("Initial queue:", char)

# Enqueue: adds an element to the end of the queue
char.append(4)
print("After enqueue 4:", char)

# Enqueue at the front (not typical for queues, but for demonstration)
char.appendleft(6)
print("After enqueue 6 at the front:", char)

# Peek: view the front element without removing it
print("Peek at the front element:", char[0])

# Dequeue: removes an element from the front
char.popleft()
print("After dequeue:", char)

# Final note
# Enqueue adds an element to the end of the queue.
# Dequeue removes an element from the front.
# Peek shows the front element without removing it.
