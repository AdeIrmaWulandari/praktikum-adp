import os
import time
from termcolor import colored

def bersih_layar():
    os.system('cls')

def tampilkan_ikon():
    print(colored("==============================================================================","cyan"))   
    print(colored("                                 SELAMAT DATANG DI                          ",'yellow',attrs=['bold']))
    print(colored("                                  APLIKASI KEREN                            ",'cyan',attrs=['bold']))
    print(colored("==============================================================================","cyan"))   

def loading_aplikasi():
    print(colored("\n Memuat Aplikasi......",'green',attrs=['bold']))
    for i in range(1,21):
        bar = "=" * i + ">" + " "*(20-i)
        persen = int((i/20)*100)
        print(colored(f'\r[{bar}]{persen}%','magenta'),end = ' ',flush=True)
        time.sleep(0.4)
    print()
    print(colored("\nSelesai!",'green'))
    
bersih_layar()
tampilkan_ikon()
loading_aplikasi()
print(colored("\nAplikasi siap digunakan!",'yellow',attrs=['bold']))