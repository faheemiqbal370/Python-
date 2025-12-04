class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def second_largest(head):
    if not head or not head.next:
        return None

    first = second = float('-inf')
    temp = head

    while temp:
        if temp.data > first:
            second = first
            first = temp.data
        elif first > temp.data > second:
            second = temp.data
        temp = temp.next

    return second if second != float('-inf') else None



head = Node(10)
head.next = Node(30)
head.next.next = Node(20)
head.next.next.next = Node(50)

print("Second Largest:", second_largest(head))
