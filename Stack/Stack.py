# Stack using LinkedList

class Node:

    def __init__(self, Value):
        self.data = Value
        self.next = None


class Stack:    # LIFO

    def __init__(self):
        self.Head = None
        self.Count = 0


    def Push(self, No):   # InsertFirst
        newn = Node(No)

        if(self.Head == None):
            self.Head = newn

        else:
            newn.next = self.Head
            self.Head = newn

        self.Count += 1



    def Pop(self):      # DeleteFirst
        if(self.Head == None):
            print("Stack is empty")
            return
        
        else:
            Value = self.Head.data
            self.Head = self.Head.next

        self.Count -= 1
        return Value


    def Display(self):
        print("Elements of the Stack are : ")

        temp = self.Head

        while(temp != None):
            print(temp.data)
            temp = temp.next


    def Count(self):
        return self.Count
    


def main():
    iObj = Stack()

    iObj.Push(10)
    iObj.Push(20)
    iObj.Push(30)
    iObj.Push(40)

    iObj.Display()

    print("Poped element is : ",iObj.Pop())

    iObj.Display()


if __name__ == "__main__":
    main()