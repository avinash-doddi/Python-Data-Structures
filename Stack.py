class Stack:
  
  def __init__(self, size):
    self.stack = []; 
    self.maxsize = size;
    self.size = 0;
  
  def push_back(self, value):
    if (self.size == self.maxsize): 
      print("Stack is full, Delete some elements and Try Again!!");
    else:
      self.stack.append(value); 
      self.size += 1;
   
  def isEmpty(self):
    if (self.size == 0): 
      return 1;
    return 0;
  
  def pop(self):
    if (self.size == 0): 
      print("Stack is Empty! Insert a few elements.");
    else:
      del self.stack[self.size - 1];
      self.size -= 1;
   
 #creating Object:
      
obj = Stack(size = 10);
