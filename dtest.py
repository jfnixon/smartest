# This is a quick and dirty disk tester
#
# The problem is macos now requires permission to access the entire disk. Full Disk Access needs
# to be granted. Even root doesn't have permissions.
# [Errno 1] Operation not permitted: '/dev/disk1'
# [Errno 2] No such file or directory: '/dev/disk2'
# [Errno 2] No such file or directory: '/dev/disk3'

import os

possible_drives = [
        "/dev/rdisk1", #MacOSX 
        "/dev/rdisk2",
        "/dev/rdisk3",
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