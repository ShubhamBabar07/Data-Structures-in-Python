# Queue using LinkedList

class Node:

    def __init__(self, Value):
        self.data = Value
        self.next = None


class Queue:    # FIFO

    def __init__(self):
        self.Head = None
        self.Count = 0


    def EnQueue(self, No):   # InsertLast
        newn = Node(No)

        if(self.Head == None):
            self.Head = newn

        else:
            temp = self.Head

            while(temp.next != None):
                temp = temp.next

            temp.next = newn

        self.Count += 1



    def DeQueue(self):      # DeleteFirst
        if(self.Head == None):
            print("Queue is empty")
            return
        
        else:
            Value = self.Head.data
            self.Head = self.Head.next

        self.Count -= 1
        return Value


    def Display(self):
        print("Elements of the Queue are : ")

        temp = self.Head

        while(temp != None):
            print(temp.data, end = "\t")
            temp = temp.next

        print("")


    def Count(self):
        return self.Count
    


def main():
    iObj = Queue()

    iObj.EnQueue(10)
    iObj.EnQueue(20)
    iObj.EnQueue(30)
    iObj.EnQueue(40)

    iObj.Display()

    print("Removed element is : ",iObj.DeQueue())

    iObj.Display()


if __name__ == "__main__":
    main()