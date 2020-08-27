
a =""
c =""
f =""
i =""
import os
import time
import argparse
import sys
import platform
colors = True  # Output should be colored
machine = sys.platform  # Detecting the os of current system
checkplatform = platform.platform() # Get current version of OS
if machine.lower().startswith(('os', 'win', 'darwin', 'ios')):
    colors = False  # Colors shouldn't be displayed in mac & windows
if checkplatform.startswith("Windows-10") and int(platform.version().split(".")[2]) >= 10586:
    colors = True
    os.system('')   # Enables the ANSI
if not colors:
    end = red = white = green = yellow = run = bad = good = info = que = ''
else:
    white = '\033[97m'
    green = '\033[92m'
    red = '\033[91m'
    yellow = '\033[93m'
    end = '\033[0m'
    blue = '\033[93m'
    reset ='\033[0m'
    back = '\033[7;91m'
    info = '\033[93m[!]\033[0m'
    que = '\033[94m[?]\033[0m'
    bad = '\033[91m[-]\033[0m'
    good = '\033[92m[+]\033[0m'
    run = '\033[97m[~]\033[0m'
logo =f"""
{yellow}
 _____ _____  
|_   _|  __ \ 
  | | | |__) |
  | | |  ___/ 
 _| |_| |     
|_____|_|     
{end}
{yellow}usage:{end} iplist.py [-h] [-a A_] [-b B_] [-c C_] [-d D_]
{red}Version:1.3{end}
{green}By:@SMDD{end}
"""
def main():
    global a
    global c
    global f
    global i
    print(logo)
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-a','--A-IP', help='IP A.x.x.x',
                            dest='a_', type=int)
        parser.add_argument('-b','--B-IP', help='IP x.B.x.x',
                            dest='b_', type=int)
        parser.add_argument('-c','--C-IP', help='IP x.x.C.x',
                            dest='c_', type=int)
        parser.add_argument('-d','--D-IP', help='IP A.x.x.D',
                            dest='d_', type=int)
        args = parser.parse_args()
        a = args.a_
        c = args.b_
        f = args.c_
        i = args.d_
        iplist()
    except:
        print(f"{bad}Error")
        exit()
def iplist():
    global a
    global c
    global f
    global i
    open("iplist.txt","w")
    for b in range(a,256):
        for d in range(c,256):
            for e in range(f,256):
                for h in range(i,256):
                    b_ =str(b)
                    d_ =str(d)
                    e_ = str(e)
                    h_ = str(h)
                    file_ = open("iplist.txt","a")
                    file_.write(str(b_)+"."+str(d_)+"."+str(e_)+"."+str(h_)+"\n")
    print(f"{good}Sava File:Iplist.txt")
main()

