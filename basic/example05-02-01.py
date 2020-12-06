import random 

a=random.randint(0,9)
print(a)

b=int(input("数を入れてね＞"))
if a == b:
  print("あたり")
else:
  print("外れ")