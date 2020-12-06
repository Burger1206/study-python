def tashizan(a,b):
  total=0
  for i in range(a,b+1):
    total=total+i
  return total

c=tashizan(1,5)
print(c)


a="abc"

def test():
  a="def"
  print(a)
  return

test()
print(a)