def insertionsort(list):
  for i in range(1, len(list)):
    temp = list[i]
    j = i-1
    while (j >= 0 and temp < list[j]):
      list[j + 1] = list[j]
      j = j - 1
    list[j + 1] = temp
  return list

list = []
n = int(input("Enter the number of elements : "))
print("Enter elements : ")
for i in range(n):
  list.append(int(input()))

print(insertionsort(list)) 
