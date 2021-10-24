import os
import sys # to get command line arguments


if len(sys.argv) == 2:
  # check if any file name is passed from command line
  file = sys.argv[1]
else:
  file=input("ENTER YOUR FILE NAME HERE:")
try: 
  os.path.isfile(file)
except:
  print("ERROR: File does not exist!")
  

    
