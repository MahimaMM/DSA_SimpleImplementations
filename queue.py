class queue:

  def __init__(self):
    self.elements = [] 

  def isEmpty(self) -> bool:
    return True if (len(self.elements) == 0) else False

  def enque(self,a):
    self.elements.append(a)

  def deque(self):
    if (self.isEmpty()):
      print("Queue is empty")
    else:
      print("Element dequeued : ",self.elements[0])
      del self.elements[0]
     
  def display(self):
      print("Queue is empty" if (self.isEmpty()) else self.elements)
  
q = queue()
print("Choose your option.... \n1. Enque \n2. Deque \n3. Display \n4. Exit")
while 1:
  option = int(input("\nOPTION : "))
  if (option == 1):
    print("\n....ENQUE....")
    q.enque(int(input("Enter the element : ")))
  elif (option == 2):
    print("\n....DEQUE....")
    q.deque()
  elif (option == 3):
    print("\n....DISPLAY....")
    q.display()
  elif (option == 4):
    break
  else :
    print("Choose correct option....")
