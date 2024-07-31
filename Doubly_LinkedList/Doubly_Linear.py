# Doubly Linear Linkedlist

class Node:

    def __init__(self, Value):
        self.data = Value
        self.next = None
        self.prev = None


class DoublyLL:

    def __init__(self):
        self.Head = None
        self.Count = 0
    

    def InsertFirst(self, No):
        newn = Node(No)

        if(self.Head == None):
            self.Head = newn

        else:
            newn.next = self.Head
            self.Head.prev = newn
            self.Head = newn

        self.Count += 1

    
    def InsertLast(self, No):
        newn = Node(No)

        if(self.Head == None):
            self.Head = newn

        else:
            temp = self.Head

            while(temp.next != None):
                temp = temp.next

            temp.next = newn
            newn.prev = temp

        self.Count += 1


    def Display(self):
        print("Elements of the LinkedList are : ")

        temp = self.Head

        print("NULL<=>", end = "")

        while(temp != None):
            print("| {0} |<=>".format(temp.data), end = "")
            temp = temp.next

        print("NULL")


    def CountNode(self):
        return self.Count
    

    def DeleteFirst(self):
        if(self.Head == None):
            print("LL is empty")
            return
        
        elif(self.Head.next == None):
            self.Head = None
        
        else:
            self.Head = self.Head.next
            self.Head.prev = None

        self.Count -= 1


    def DeleteLast(self):
        if(self.Head == None):
            print("LL is empty")
            return
        
        elif(self.Head.next == None):
            self.Head = None

        else:
            temp = self.Head

            while(temp.next.next != None):
                temp = temp.next

            temp.next = None

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
    iObj = DoublyLL()

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