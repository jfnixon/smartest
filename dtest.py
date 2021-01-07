# This is a quick and dirty disk tester
import os

possible_drives = [
        "/dev/disk1", #MacOSX 
        "/dev/disk2",
        "/dev/disk3",
        ]

SECTOR_SIZE = 512
BUFFER_SIZE = 1024*SECTOR_SIZE
buf = bytearray(BUFFER_SIZE)

for drive in possible_drives:
    try:
        fd = os.open(drive, os.O_RDONLY)
        ### os.write(fd, buf)
        os.read(fd, 16)
    except:
        pass