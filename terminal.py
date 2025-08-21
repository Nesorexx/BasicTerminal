import os
import platform
import getpass

def Unix():
 print("Operating system:",platform.system())
 print("User:",getpass.getuser())
 inbuilt = getpass.getuser()+"$ "
 def commands():
  os.system(input(inbuilt))
 while True:
  commands()

def Windows():
 print("Operating system:",platform.system())
 print("User:",getpass.getuser())
 inbuilt = getpass.getuser()+"$ "
 def command():
  os.system(input(inbuilt))
 while True:
  command()

if platform.system() == "Linux" or platform.system == "Darwin":
 while True:
  Unix()

elif platform.system() == "Windows":
 while True:
  Windows()
  
