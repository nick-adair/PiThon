import socket
import sys
import time

def blink(os_type,duration):

    print("LED ON")
    time.sleep(duration)
    print("LED OFF")

    return

def main():

    duration_long=500
    duration_medium=500
    duration_short=250

# First, get default route device then get ip on the default route device
    os_type = sys.platform
    hostname=socket.gethostname()
    IP=socket.gethostbyname(hostname) # this is a string


    exit ()

if __name__ == '__main__':
    main()
