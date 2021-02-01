#python language used

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
    
    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print (node.data)
            node = node.next

    def delete(self, data):
        if self.head == '':
            print ('There's no data')
            return
        if self.head.data == data: # case 1: delete self.head - change self.head
            temp = self.head # To delete self.head, create temparaty location 'temp' and delete 'temp'
            self.head = self.head.next # if delete self.head, code is not working!
            del temp
        else:
            node = self.head
            while node.next: # case 2: Not self.head, delete node
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next       
                    del temp                         
                    pass                             
                else:
                    node = node.next
                    
    def search_node(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
