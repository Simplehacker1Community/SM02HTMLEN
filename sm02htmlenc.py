
#========================================||
#================PROJECT INFO============||
#========================================||
#==== Auther : SM02 PresenT =============||
#==== Start Date : 14/11/2021 ===========||
#==== End Date : 23/04/2022 =============||
#==== Version : 1.0 BETA ================||
#==== About : htm Encoding=========||
#==== Note : Do Not Copy My Code , ======||
#==== Otherwise Deleting My project =====||
#========================================||
#================END INFO================||
#========================================||

from os import system
import time
print("████████████████████████████████")
print("█▄─██─▄█▄─▄▄─██▀▄─██─▄─▄─█▄─▄▄─█")
print("██─██─███─▄▄▄██─▀─████─████─▄█▀█")
print("▀▀▄▄▄▄▀▀▄▄▄▀▀▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀")
print("\033[31m Checking update .....")
system('cat .version.txt && rm .ping')
system('wget https://raw.githubusercontent.com/Simplehacker1Community/SM02HTMLEN/simplehacker/.ping &')
update = 'sm02'
file1 = open(".ping", "r")
readfile = file1.read()
if update in readfile:
  print("\033[31m Update Found ")
  time.sleep(1)
  print("\033[32m updateing ..")
  system("cd ..")
  system('rm -rf SM02HTMLEN')
  system('git clone htpps://github.com/simplehacker1communty/SM02HTMLEN')
  system('cd SM02HTMLEN')
  system('python run.py')
else:
  time.sleep(2)
  system('clear')
  #auther()
  print("update not found")
  system(f"xdg-open https://t.me/sm02present")
  print("\033[33mPlease visit\n \033[31m https://t.me/sm02present")
  system("python3 sm02htmlen.cpython-39.py")
        
