import os 
#this command will list the dir in the local system
files = os.listdir("images")
a = 1 

for name in files:
    if name.endswith(".jpg"):
      
      # if u want to print the grab files from the os.listdir command remove # form bellow command
        # print("\n",files)
      
      # os command will take two parameters first is the name of the file and second parameter is the name that the user wants to rename
      
        os.rename(f"images/{name}",f"images/{a}.png")
        a = a+1
