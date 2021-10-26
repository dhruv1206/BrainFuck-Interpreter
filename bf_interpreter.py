"""
---------------------------------------------------------------------------
                      BRAINFUCK INTERPRETER in Python
---------------------------------------------------------------------------
        By Dhruv Agrawal (dhruv1206) & Ashish Kushwaha (AshishKingdom)
"""

import os
import math
import sys # to get command line arguments


if len(sys.argv) == 2:
  # check if any file name is passed from command line
  file = sys.argv[1]
else:
  file=input("ENTER YOUR FILE NAME HERE:")

if os.path.isfile(file):
  # File exists
  program_file = open(file, 'r')
  program_data = ''.join(program_file.read().split('\n'))
  program_file.close()
else:
  # File does not exists
  print("ERROR: File does not exist!")
  # we need to terminate program if file doesn't exists
  exit()

my_arr=[0]*30000
index=0
pos = 0
max_position = len(program_data)
while pos<max_position:
  data = program_data[pos]
  if data==">":
    if index>=30000:
      print("MAXIMUM value of index reached!")
      break
    else:
      index+=1

  elif data=="<":
    if index<0:
      print("No Previous Element Found!")
      break
    else:
      index-=1

  elif data=="+":
    my_arr[index]+=1
    if my_arr[index]>255:
      my_arr[index] = 0

  elif data=="-":
    my_arr[index]-=1
    if my_arr[index]<0:
      my_arr[index] = 255

  elif data==".":
    print(chr((my_arr[index])) , end="")

  elif data==",":
    my_arr[index]=ord(input("ENTER A CHARACTER:"))
  elif data=="[":
    if my_arr[index]==0:
      a = 1
      while a!=0:
        pos += 1
        if program_data[pos]=="[": a += 1
        if program_data[pos]=="]": a -= 1
        if pos>=max_position:
          print("No closing ']' found!")
          break
  elif data=="]":
    if my_arr[index]!=0:
      a = 1
      while a!=0:
        pos -= 1
        if program_data[pos]=="[": a -= 1
        if program_data[pos]=="]": a += 1
        if pos<=0:
          print("No opening '[' found!")
          break

  pos += 1