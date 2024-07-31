# Doubly Circular Linkedlist

class Node:

    def __init__(self, Value):
        self.data = Value
        self.next = None
        self.prev = None


class DoublyCL:

    def __init__(self):
        self.Head = None
        self.Tail = None
        self.Count = 0
    

    def InsertFirst(self, No):
        newn = Node(No)

        if((self.Head == None) and (self.Tail == None)):
            self.Head = newn
            self.Tail = newn

        else:
            newn.next = self.Head
            self.Head.prev = newn
            self.Head = newn

        self.Tail.next = self.Head
        self.Head.prev = self.Tail

        self.Count += 1

    
    def InsertLast(self, No):
        newn = Node(No)

        if((self.Head == None) and (self.Tail == None)):
            self.Head = newn
            self.Tail = newn

        else:
            self.Tail.next = newn
            newn.prev = self.Tail
            self.Tail = newn

        self.Tail.next = self.Head
        self.Head.prev = self.Tail

        self.Count += 1


    def Display(self):
        if((self.Head == None) and (self.Tail == None)):
            print("LL is Empty")
            return

        print("Elements of the LinkedList are : ")

        print("<=>", end = "")

        while True:
            print("| {0} |<=>".format(self.Head.data), end = "")
            self.Head = self.Head.next

            if(self.Head == self.Tail.next):
                break;

        print("")


    def CountNode(self):
        return self.Count
    

    def DeleteFirst(self):
        if((self.Head == None) and (self.Tail == None)):
            print("LL is empty")
            return
        
        elif(self.Head == self.Tail):
            self.Head = None
            self.Tail = None
        
        else:
            self.Head = self.Head.next
            self.Tail.next = self.Head
            self.Head.prev = self.Tail

        self.Count -= 1


    def DeleteLast(self):
        if((self.Head == None) and (self.Tail == None)):
            print("LL is empty")
            return
        
        elif(self.Head == self.Tail):
            self.Head = None
            self.Tail = None

        else:
            self.Tail = self.Tail.prev
            self.Tail.next = self.Head
            self.Head.prev = self.Tail

        self.Count -= 1


    def InsertAtPos(self, No, Pos):
        if((Pos < 1) or (Pos > self.Count + 1)):
            print("Invalid Position")
            return
        
        if(Pos == 1):
            self.InsertFirst(No)

        elif(Pos == self.Count + 1):
            self.InsertLast(No)

        else:
            temp = self.Head
            newn = Node(No)

            for i in range(1,Pos-1):
                temp = temp.next

            newn.next = temp.next
            temp.next.prev = newn
            temp.next = newn
            newn.prev = temp

            self.Count += 1

            
    def DeleteAtPos(self,Pos):
        if((Pos < 1) or (Pos > self.Count)):
            print("Invalid Position")
            return
        
        if(Pos == 1):
            self.DeleteFirst()

        elif(Pos == self.Count):
            self.DeleteLast()

        else:
            temp = self.Head

            for i in range(1,Pos-1):
                temp = temp.next

            temp.next = temp.next.next
            temp.next.prev = temp

            self.Count -= 1



def main():
    iObj = DoublyCL()

    iObj.InsertFirst(101)
    iObj.InsertFirst(51)
    iObj.InsertFirst(21)
    iObj.InsertFirst(11)

    iObj.InsertLast(111)
    iObj.InsertLast(121)
    iObj.InsertLast(151)
    
    iObj.Display()
    print("Number of Nodes are : %d" %iObj.CountNode())

    iObj.InsertAtPos(105, 5)
    iObj.Display()
    print("Number of Nodes are : %d" %iObj.CountNode())

    iObj.DeleteAtPos(5)
    iObj.Display()
    print("Number of Nodes are : %d" %iObj.CountNode())


if __name__ == "__main__":
    main()