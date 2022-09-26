import os


file_name = " "
x = 0

t=0
while t <=1:
     f = open(f"{file_name}%s.txt" % x, 'w+')
     x += 1
     for i in range(1):
          f.write("aristocrat doesn't belong")
