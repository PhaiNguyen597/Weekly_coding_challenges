#We have to create a linked list in Python

class Node:
    def __init__(self, data = None):
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

def intersect(list1, list2):
    curr1 = list1.headval
    curr2 = list2.headval
    for i in range(list1.length()):
        curr2 = list2.headval
        for j in range(list2.length()):
            if curr2 is not None and curr1 is not None:
                try:
                    print(f"comparing {curr2.next.data} and {curr1.next.data}")
                    if curr2.next.data == curr1.next.data:
                        return True
                    if curr1.data == list2.headval:
                        return True
                    if curr2.data == list1.headval:
                        return True
                except:
                    pass
            curr2 = curr2.next
        curr1 = curr1.next
    return False

if __name__ == "__main__":
    list = LinkedList()
    list2 = LinkedList()
    list3 = LinkedList()
    list4 = LinkedList()
    node_list = [] #1-5
    node_list2 = [] #5-10
    node_list3 = [] #even
    node_list4 = [] #odd
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
        if i <=4:
            node_list[i].next = node_list[i+1]
    for i in range(len(node_list2)):
        list2.headval = node_list2[0]
        list2.headval.next = node_list2[1]
        if i <=4:
            node_list2[i].next = node_list2[i+1]
    for i in range(len(node_list3)):
        list3.headval = node_list3[0]
        list3.headval.next = node_list3[1]
        if i <=4:
            node_list3[i].next = node_list3[i+1]
    for i in range(len(node_list4)):
        list4.headval = node_list4[0]
        list4.headval.next = node_list4[1]
        if i <=4:
            node_list4[i].next = node_list4[i+1]


            
    print("list1")
    list.printlist()
    print("list2")
    list2.printlist()
    print("list3")
    list3.printlist()
    print("list4")
    list4.printlist()
    print(intersect(list, list2))
    print(intersect(list3, list4))
    print(intersect(list, list3))
