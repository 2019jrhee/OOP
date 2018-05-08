class Queue ():

# __init__
    def __init__(self):
        self.items = []

# enqueue: insert items to the queue
    def enqueue(self,item):
        self.items.insert(0,item)

# dequeue: take out items from the queue
    def dequeue(self):
        self.items.pop()

# list the items in the queue
    def list_items(self):
        for items in self.items:
            print(items)

#q is an instance for the class Queue
q= Queue()
#insert the word () to the queue
q.enqueue ('orange')
#insert the number () to the queue
q.enqueue (56)
#print list of items in the queue
print (q.list_items())
#take out the items from the queue
q.dequeue()
print (q.list_items())
