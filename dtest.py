# This is a quick and dirty disk tester
import os

possible_drives = [
        "/dev/disk1", #MacOSX 
        "/dev/disk2",
        "/dev/disk3",
        ]

SECTOR_SIZE = 512
BUFFER_SIZE = 1024*SECTOR_SIZE
buf1 = bytearray(BUFFER_SIZE)
buf2 = bytearray(BUFFER_SIZE)

for drive in possible_drives:
    try:
        fd = os.open(drive, os.O_RDONLY)
        br = 1

        while br > 0:
            br = os.readv(fd, [buf1, buf2])
            btotal += br
            print(">> read {btotal} bytes", end='\r')

    except IOError as error:
        print(error)