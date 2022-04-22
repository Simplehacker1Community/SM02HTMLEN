from os import system
import time
print("████████████████████████████████")
print("█▄─██─▄█▄─▄▄─██▀▄─██─▄─▄─█▄─▄▄─█")
print("██─██─███─▄▄▄██─▀─████─████─▄█▀█")
print("▀▀▄▄▄▄▀▀▄▄▄▀▀▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀")
print("\033[31m Checking update .....")
system('cat .version')
system('wget -q https://raw.githubusercontent.com/Simplehacker1Community/SM02HTMLEN/simplehacker/.ping &> /div/null')
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
  system('python sm02htmlenc.py')
else:
  time.sleep(2)
  system('clear')
  #auther()
  print("update not found")
  system(f"xdg-open https://t.me/sm02present")
  print("\033[33mPlease visit\n \033[31m https://t.me/sm02present")
  system("python3 sm02htmlen.cpython-39.pyc")
        
