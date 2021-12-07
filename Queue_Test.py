from Queue import Queue


from Queue import Queue

print("-----enqueue-----")
test_queue = Queue()
test_queue.enqueue(1)
test_queue.enqueue(2)
test_queue.enqueue(3)
print(test_queue.stringify())

print("-----peek-----")
test_queue = Queue()
print(test_queue.peek())
test_queue.enqueue(1)
print(test_queue.peek())

print("-----pop-----")
test_queue = Queue()
test_queue.enqueue(1)
test_queue.enqueue(2)
test_queue.enqueue(3)
print(test_queue.pop())
print(test_queue.pop())
print(test_queue.pop())
print(test_queue.pop())