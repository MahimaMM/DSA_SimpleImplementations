#Balenced Bracket check using Stack
class balbracketstack:
  def __init__(self):
    self.elements = [] 
  def isEmpty(self) -> bool:
    return True if (len(self.elements) == 0) else False
  def push(self,a):
    self.elements.append(a)
  def pop(self):
    if (not self.isEmpty()):
      e = self.elements[len(self.elements)-1]
      self.elements.pop()
      return e
  def display(self):
    print("Stack is empty" if (self.isEmpty()) else self.elements)

s = balbracketstack()
str = input("Enter your string : ")
not_balenced = 0
for i in str:
  if (i == '(') or (i == '[') or (i == '{'):
    s.push(i)   
  elif (i == ')'):
    e = s.pop() 
    if (e!='('):
      print ("String not balenced")
      not_balenced = 1
      break
  elif (i == '}'): 
    e = s.pop() 
    if (e!='{'):
      print ("String not balenced")
      not_balenced = 1
      break
  elif (i == ']'):
    e = s.pop() 
    if (e!='['):
      print ("String not balenced")
      not_balenced = 1
      break
if (len(s.elements) == 0):
  if not_balenced == 0:
    print ("String is balenced")
else:
  print ("String not balenced")
