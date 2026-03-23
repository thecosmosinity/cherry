# Created on 23/06/2024 by midnight
# Don't use this for tracking people that don't want to be tracked!

import geocoder
selfip = geocoder.ip('me')

def getmyip():
    uinip = input("do you want your location (approx.) with ip? (y/n): ")
    if uinip == "y":
        print(selfip.ip, selfip.city, selfip.latlng)
    elif uinip =="n":
        print(selfip.ip)
    else:
        return 'Invalid input!'
    
def trackIP(track):
    if track == "": # Failsafe
        print("Invalid input!")
        return 0
    track = geocoder.ip(track)
    print("IP Tracked!")
    print("Information about the IP is being printed...")
    print(track.ip, track.latlng, track.city)
    print("ISP", track.org)

def versionInfo():
    print("Cherry V2.0.0 By Midnight")
    print("Compiled on 23/03/26")


def console():
    print("""

    Welcome to CherryV2 by Midnight!
    1. Track yourself
    2. Track IP
    3. Version Info
    X. Exit

""")
    
    u = str(input())
    if u == "1":
        getmyip()
    elif u =="2":
        x = str(input("Enter an IP to track: "))
        trackIP(x)
    elif u =="3":
        versionInfo()
    elif u =="X":
        print("Goodbye!")
        exit()

while True:
    console()