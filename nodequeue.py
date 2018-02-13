class Node:
    def __init__(self, data):
        self.data= data
        self.next= None
        
class queue:
    def __init__(self,data):
        self.head=Node(data)

    def enqueue(self,data):
        newNode=Node(data)
        temp=self.head
        while temp.next != None:
            temp=temp.next
        temp.next=newNode

    def dequeue(self):
        print(self.head.data)
        self.head=self.head.next
        #temp=self.head
        #while temp.next!=None:
            #temp=temp.next
        

    def printq(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next

    def size(self):
        counts=0
        temp=self.head
        while temp!=None:
            counts+=1
            temp=temp.next
        print(counts)

#q=queue(1)
#q.enqueue(2)
#q.enqueue(3)
#q.printq()
#q.dequeue()
#q.size()
#q.dequeue()
#q.dequeue()
#q.size()
