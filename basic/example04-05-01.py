for a in range(1,10+1):
  if a<=5:
    print("小さいです")
  else:
    print("大きいです")
  

for a in range(1,10+1):
  if a%2==0:
    print("○")
  
  elif a%3==0:
    print("✖︎")
  
  elif a%2==0 and a%3==0:
    print("△")

  else:
    print("何も表示しない")