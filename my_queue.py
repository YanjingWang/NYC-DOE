from myLinkedList import ListNode
from queue import Queue
# queue is FIFO

class MyQueue():
    def __init__(self):
        self.count = 0  # how many values now
        self.head = None
        self.tail = None

    def enqueue(self, value):
        node = ListNode(value)
        if self.head is None: # if queue is empty
            self.head = node
            self.tail = node

        else:
            self.tail.next = node # tail points to new node
            self.tail = node # tail points to new node
        self.count += 1

    def dequeue(self):
        if self.head is None: 
            raise Exception('this is an empty queue')
        cur = self.head  # store queue head
        self.head = cur.next  # queue head points to next
        self.count -= 1
        return cur.val

    def is_empty(self):
        return self.head is None  # self.count == 0

    def size(self):
        return self.count


if __name__ == '__main__':
    my_queue = MyQueue()
    for i in range(50):
        my_queue.enqueue(i)
    
    while not my_queue.is_empty():
        print(my_queue.dequeue(),end = ' ')

    # use Queue module
    # que = Queue()
    # for i in range(50):
    #     que.put(i)  # Queue module's enqueue method is put()

    # while not que.empty():
    #     print(que.get(), end=' ')  #Queue module's dequeue is get()
    # print()
    # print(que.qsize())  # size of Queue module

    from queue import Queue
    que = Queue(maxsize=100) # maxsize < 1 is infinite
    for i in range(50):
        que.put(i)
    while not que.empty():
        print(que.get(), end=' ')
    # print()
    # print(que.qsize())  # size of Queue module
    # print(que.full())  # is full
    # print(que.empty())  # is empty
    # print(que.maxsize)  # maxsize of Queue module
    # print(que.queue)  # queue of Queue module
    # print(que.get())  # get from Queue module


