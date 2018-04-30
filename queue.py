class Queue ():

# __init__
    def __init__(self):
        self.items = []

# enqueue
    def enqueue(self,item):
        self.items.insert(0,item)

# dequeue
    def dequeue(self):
        self.items.pop()


    def list_items(self):
        for items in self.items:
            print(items)

q= Queue()
q.enqueue ('orange')
q.enqueue (56)
print (q.list_items())
q.dequeue()
print (q.list_items())
