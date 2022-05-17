class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # Initialize next as null

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

def reverse_list(list):
    previous = None
    current = list.head
    following = current.next

    while current is not None:
        following = current.next
        current.next = previous
        previous = current
        current = following

    list.head = previous

if __name__ == '__main__':
    my_list = LinkedList()
    my_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Link first node with the second
    my_list.head.next = second
    second.next  = third

    # Print list
    my_list.print_list()
    reverse_list(my_list)
    print("\nReversed list")
    my_list.print_list()

