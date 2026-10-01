# Create node
# Create linked list
# Add nodes to linked list
# Print linked list


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # head => Jhon -> None
    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            # head => Jhon -> Ben -> None
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        if self.head is None:
            print("List is empty")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next


# Node -> data, nect
# firstnode.data -> Jonh
# firstnode.next -> None

firstNode = Node("John")
linkedList = LinkedList()
linkedList.insert(firstNode)
secondNode = Node("Ben")
linkedList.insert(secondNode)
thirdNode = Node("Mathew")
linkedList.insert(thirdNode)
linkedList.printList()
