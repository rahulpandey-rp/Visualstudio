class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return(f"{self.data} is pointing to {self.next}")


class LinkedList:
    def __init__(self, data):
        self.head = data[0]
        self.data = data
        self.linked_list = [
                            Node(self.data[index], self.data[index + 1])
                            for index in range(0, len(self.data) - 1)
                            ]
        self.linked_list.append(Node(self.data[-1]))

    def __repr__(self):
        return(f"{self.linked_list}")


list_1 = LinkedList([1, 2, 3, 4])
print(list_1)
