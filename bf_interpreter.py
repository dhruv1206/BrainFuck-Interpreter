import os

file=input("ENTER YOUR FILE HERE:")
try: 
  os.path.isfile(file)
except:
  print("ERROR: File does not exist!")
  

    
