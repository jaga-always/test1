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
    q.enqueue(11)
    q.enqueue(12)
    q.enqueue(13)
    print("Front" ,q.front())
    print("Deque")
    print(q.dequeue())
    print(q.dequeue())
    print("Size",q.size())
    end = time.time()
    print(f"Runtime of the programm is{end-start}")
            

    
 
