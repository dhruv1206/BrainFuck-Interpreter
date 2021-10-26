import os
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

my_arr=[0]*30000
index=0
if len(program_data)<=30000:
  for data in program_data:

    if data==">":
      index+=1

    elif data=="<":
      if index==0:
        print("No Previous Element Found!")
        break
      else:
        index-=1

    elif data=="+":
      my_arr[index]+=1

    elif data=="-":
      my_arr[index]-=1

    elif data==".":
      print(chr(my_arr[index]) , end="")

    elif data==",":
      my_arr[index]=ord(input("ENTER A CHARACTER:"))
else:
  print("File is too large to handle!")
