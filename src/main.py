'''
    IpWin - Windows Ip App 
    Version - Completed Рroject
        Created by Lab
GitHub - https://github.com/LaunchL
Discord - https://discord.gg/ngMUeFEgQa
'''
#Imports
import socket
from time import sleep

#Code
#Start message
print("Hello! Welcome to IpWin - Windows Ip.")
print("Created by Launch Lab")
print("GitHub - https://github.com/LaunchL")
print("Discord - https://discord.gg/ngMUeFEgQa")

#What kind of IpWin?
print("IpWin - Windows Ip By Lab, is a рrogram to find out your IP Address on your device.")

#Ip Address Device
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("Your pc name: " + host_name) #Pc name - Host name
print("Your IP address: " + host_ip) #Pc ip - Host ip


#Quit
while True:
    print("Press Ctrl + C to exit.")
    sleep(5)

#Bye! 4:02 PM 1/7/2021 and I want to sleep ...