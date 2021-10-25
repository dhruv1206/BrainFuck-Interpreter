import os
import sys # to get command line arguments


if len(sys.argv) == 2:
  # check if any file name is passed from command line
  file = sys.argv[1]
else:
  file=input("ENTER YOUR FILE NAME HERE:")
try: 
  if os.path.isfile(file):
    # File exists
    program_file = open(file, 'r')
    program_data = ''.join(program_file.read().split('\n'))
    program_file.close()
  else:
    # File does not exists
    print("ERROR: File does not exist!")
except:
  print("ERROR: File does not exist!")
  

    
