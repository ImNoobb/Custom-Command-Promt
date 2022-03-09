import os
import getpass
import socket
import subprocess
from colorama import Fore,Back,Style

print('HN-Promt(R) by HN\n')
current = os.getcwd()
path = current + '\\r_cd.bat'

while True:
       string = Back.BLACK + Fore.CYAN + ' ' +"ImNoobb" + Back.CYAN + Fore.BLACK+ ""+"  " + socket.gethostname() + Fore.CYAN + Back.GREEN + ""+Fore.BLACK+Back.GREEN+"  " + current.replace('C:\\Users\\Hua Hoang Anh','~ ') + Fore.GREEN + Back.RESET+ " "+Fore.RESET+Back.RESET
       cmd = input(string)
       if cmd == 'cd..' or cmd == 'cd ..':
              current = subprocess.check_output([path,f'{current}','..'], shell=True).decode().replace('\r\n','')
              os.chdir(current)
       elif 'cd ' in cmd:
              current = subprocess.check_output([path,f'{current}',f"{cmd.replace('cd ','')}"], shell=True).decode().replace('\r\n','')
              os.chdir(current)
       elif 'd:' in cmd or 'D:' in cmd:
              current = 'D:\\'
              os.chdir(current)
       elif cmd == 'exit':
              break
       else:
              os.system(cmd)