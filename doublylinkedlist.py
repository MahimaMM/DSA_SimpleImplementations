class node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class doublylinkedlist:
  def __init__(self):
    self.head = None
  def insert(self, data, case):
    newnode = node(data)
    if (self.head is None and case !=2): 
      self.head = newnode
    #Insertion at the beginning
    elif (case == 1):
      newnode.next = self.head
      self.head.prev = newnode
      self.head = newnode
    #Insertion after a reference value 
    elif (case == 2):
      if (self.head is None):
        print("Empty Linked List")
      else:
        refvalue = input("Reference Value : ")
        valuefound = False
        current = self.head
        while (current):
          if(current.data == refvalue):
            valuefound = True
            newnode.next = current.next
            newnode.prev = current
            if current.next is not None:
              current.next.prev = newnode
            current.next = newnode
            break
          current = current.next
        if not valuefound:
          print("Reference Not Found !")
    #Insertion at the end
    elif (case == 3):
      current = self.head 
      while (current.next is not None):
        current = current.next
      current.next = newnode
      newnode.prev = current
  def delete(self, case):
    if (self.head is None): 
      print("Empty Linked List")
    #Deletion at the beginning
    elif (case == 1):
      self.head = self.head.next
      if self.head is not None:
        self.head.prev = None
    #Deletion of a reference value 
    elif (case == 2):
      valuefound = False
      refvalue = input("Reference Value : ")
      current = self.head
      while (current):
        if(current.data == refvalue):
          valuefound = True
          if (self.head.next is None):
            self.head = None
          else:
            if current.prev is None:
              self.head = current.next
            else: 
              current.prev.next = current.next
            if current.next is not None:
              current.next.prev = current.prev
          break
        current = current.next
      if not valuefound:
        print("Reference Not Found !")
    #Deletion at the end
    elif (case == 3):
      current = self.head 
      while (current.next is not None):
        current = current.next
      if (self.head.next is None):
        self.head = None
      else:
        current.prev = None #Notmadatory
        current.prev.next = None
  def traverse(self):
    current = self.head
    print("Head  [next]->  ", end = "")
    while (current):
      print(current.data," [next]->  ", end = "")
      if current.next is not None:
        current = current.next
      else: 
        break
    print("None ")
    while (current):
      print(current.data," [prev]->  ", end = "")
      current = current.prev
    print("Head  [prev]->  None")
      
sll = doublylinkedlist()
print("Choose your option.... \n1. Insert \n2. Delete \n3. Traverse \n4. Exit")
while 1:
  option = int(input("\nOPTION : "))
  if (option == 1):
    print("\n....INSERT....")
    data = input("Enter the element : ")
    case = int(input("1.Beginning 2.After_Reference 3.End | CASE : "))
    sll.insert(data, case)
  elif (option == 2):
    print("\n....DELETE....")
    case = int(input("1.Beginning 2.Reference_Value 3.End | CASE : "))
    sll.delete(case)
  elif (option == 3):
    print("....DOUBLY LINKED LIST TRAVERSE....")
    sll.traverse()
  elif (option == 4):
    break
  else :
    print("Choose correct option....")
