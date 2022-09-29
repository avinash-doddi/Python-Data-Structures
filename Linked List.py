class Node:
    
    def __init__(self):
        self.data = 0;
        self.next = None;
    
class LinkedList:
    
    def __init__(self):
        self.head = None;
        self.temp = None;
        
    def insert(self, value):
        self.newnode = Node();
        self.newnode.data = value;
        if (self.head == None):
            self.head = self.newnode;
            self.temp = self.newnode;
            
        else:
            self.temp.next = self.newnode;
            self.temp = self.newnode;
    
    def search(self, key):
        if (self.head == None):
            return "Linked List is Empty";
        else:
            temp = self.head;
            while(temp != None):
                if (temp.data == key):
                    return "key found";
                temp = temp.next;
            return "key not found";
    
i = LinkedList();
print(i.search(2));
i.insert(10);
i.insert(20);
i.insert(30);
print(i.search(20));
