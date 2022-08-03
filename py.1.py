import time
start = time.time()
class Queue:
    def__init__(self) :
    self.items=[]
    def isEmpty(self):
     return self.items ==[]
    def enqueue(self,item):
            self.items.append(item)
            prnt(item)
    def dequeue(self):
     return self.items.pop(O)
    def front(self):
     return self.items[len(self.items)-1]
     def size(self):
      return len(self.items)
    q=Queue()
    print(q.isEmpty(),"-because queue is empty")
    print("Enquee")
    q.enqueue(15)
    q.enqueue(16)
    q.enqueue(17)
    print("Front" ,q.front())
    print("Deque")
    print(q.dequeue())
    print(q.dequeue())
    print("Size",q.size())
    end = time.time()
    print(f"Runtime of the programm is{end-start}")
            

    
 
