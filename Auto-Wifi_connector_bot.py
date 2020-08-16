#connects to already saved wifi network

#netsh is a command line scripting utility which allows you to display or modify the network configuration 
#Running netsh command from inside a program
#os.popen(); opens a pipe to or from command and returns an open file object connected to the  pipe, which can be read or written

import os
import sys


#Step 1 - > check for saved networks 
saved_profiles = os.popen('netsh wlan show profiles').read()
print(saved_profiles)

#Step 2 -> check for available networks
available_profiles = os.popen('netsh wlan show networks').read()

#Step 3 -> Input preferred network
preferred_ssid = input("Enter your preferrred wifi network : ")

#Step 4 -> DIsconnect currently connected network
response = os.popen('netsh wlan disconnect').read()
print(response)

if preferred_ssid not in saved_profiles:
    print("PROFILE : " + preferred_ssid + " is not saved in the system...exiting" )
    sys.exit()
elif preferred_ssid not in available_profiles:
    print("PROFILE : " + preferred_ssid + " is not available currently...trying again soon")


while True:
    avail = os.popen('netsh wlan show networks').read()
    #sleep(3)
    if preferred_ssid in avail:
        print('Network Found')
        break ; 

print('--------Connecting-----------')

response = os.popen('netsh wlan connect name=' + '"' + preferred_ssid + '"').read()
print(response)