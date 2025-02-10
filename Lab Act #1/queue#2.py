import queue

q = queue.Queue()

q.put(1)
q.put(2)
q.put(3)

print("Queue after enqueuing:")
while not q.empty():
    print(q.get())
