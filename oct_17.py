import random

# Linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.headval = None

    def printlist(self):
        printval = self.headval
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def length(self):
        curr = self.headval
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
        return count


# Stack
class Stack:
    def __init__(self):
        self.vals = []

    def push(self, val):
        self.vals.append(val)

    def size(self):
        return len(self.vals)

    def pop(self):
        if self.size() == 0:
            raise IndexError
        else:
            self.vals.pop(len(self.vals) - 1)

    def peek(self):
        length = len(self.vals)
        if length == 0:
            print("The stack is empty!")
        else:
            print(self.vals[length - 1])

    def max(self):
        if self.size() == 0:
            raise IndexError
        else:
            print(max(self.vals))


def intersect(list1, list2):
    curr1 = list1.headval
    curr2 = list2.headval
    for i in range(list1.length()):
        curr1 = list1.headval
        for j in range(list2.length()):
            if curr1 and curr2 is not None:
                if (
                    curr1.data == curr2.data
                    and curr1.data != None
                    and curr2.data != None
                ):
                    return curr1.data
                else:
                    curr1 = curr1.next
        curr2 = curr2.next
    return "No intersection"


def a():
    list = LinkedList()
    list2 = LinkedList()
    list3 = LinkedList()
    list4 = LinkedList()
    node_list = []  # 1-5
    node_list2 = []  # 5-10
    node_list3 = []  # even
    node_list4 = []  # odd
    for i in range(12):
        if i <= 5:
            node_list.append(Node(i))
        if i >= 5:
            node_list2.append(Node(i))
        if i % 2 == 0:
            node_list3.append(Node(i))
        if i % 2 == 1:
            node_list4.append(Node(i))
    for i in range(len(node_list)):
        list.headval = node_list[0]
        list.headval.next = node_list[1]
        if i <= 4:
            node_list[i].next = node_list[i + 1]
    for i in range(len(node_list2)):
        list2.headval = node_list2[0]
        list2.headval.next = node_list2[1]
        if i <= 4:
            node_list2[i].next = node_list2[i + 1]
    for i in range(len(node_list3)):
        list3.headval = node_list3[0]
        list3.headval.next = node_list3[1]
        if i <= 4:
            node_list3[i].next = node_list3[i + 1]
    for i in range(len(node_list4)):
        list4.headval = node_list4[0]
        list4.headval.next = node_list4[1]
        if i <= 4:
            node_list4[i].next = node_list4[i + 1]

    print(intersect(list2, list4))


def b():
    test = Stack()
    for i in range(10):
        test.push(random.randint(0, 100000))
    test.max()


a()
# b()
