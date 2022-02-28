class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = None
        self.data = data
        for data in self.data:
            self.inserting(data)

    def __repr__(self):
        temp = self.head
        while(temp):
            temp2 = temp.next
            if(temp2 is None):
                pointing = None
            else:
                pointing = temp2.data
            print(f"{temp.data} is pointing to {pointing}")
            temp = temp.next
        return("")

    def inserting(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node


list_1 = LinkedList([1, 2, 3, 4])
print(list_1)
