class stack:

  def __init__(self):
    self.elements = [] 

  def isEmpty(self) -> bool:
    return True if (len(self.elements) == 0) else False

  def push(self,a):
    self.elements.append(a)

  def pop(self):
    if (self.isEmpty()):
      print("Stack is empty")
    else:
      print("Element popped : ",self.elements[len(self.elements)-1])
      self.elements.pop()

  def display(self):
    print("Stack is empty" if (self.isEmpty()) else self.elements)
  
s = stack()
print("Choose your option.... \n1. Push \n2. Pop \n3. Display \n4. Exit")
while 1:
  option = int(input("\nOPTION : "))
  if (option == 1):
    print("\n....PUSH....")
    s.push(input("Enter the element : "))
  elif (option == 2):
    print("\n....POP....")
    s.pop()
  elif (option == 3):
    print("\n....DISPLAY....")
    s.display()
  elif (option == 4):
    break
  else :
    print("Choose correct option....")
