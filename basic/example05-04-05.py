import re

isok=False
while isok==False:
  b=input("数を入れてね＞")
  if not re.match(r"^\d\d\d\d$",b):
    print("４桁の数字を入れてください")
  else:
    isok=True

print(b[0])
print(b[1])
print(b[2])
print(b[3])