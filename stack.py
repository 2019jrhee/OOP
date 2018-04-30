#create a stack object that has the
#push, pop, isEmpty methods
#add 3 new methods
#list all items
#find an items# add a list to stack

class Stack:

# init
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def isEmpty(self):
        a = []
        if self.items == a:
            print ('True')
            return (True)
        else:
            print('False')
            return False


# Add 3 new methods
# list all items
    #Some type of loop
    #For vs. while
    def list_items(self):
        print("The available items are:")
        for items in self.items:
            print(items)

# Find an items
    # loop through Stack
    # if/else
    def find_items(self):

# Add a list to stack
        pass

    def b_sort(self):
        n=len(self.items)
        for x in range(n):
            for y in range(0,n-x-1):
                if self.items[y] > self.items[y+1]:
                    self.items[y], self.items[y+1] = self.items[y+1], self.items[y]
        print(self.items)

#create a new stack
dog_stack = Stack()
#populate some data

dog_stack.push(5000)
dog_stack.push(500)
dog_stack.push(5)
dog_stack.push(50)
#test to see if empty
dog_stack.isEmpty()

dog_stack.list_items()
dog_stack.b_sort()
