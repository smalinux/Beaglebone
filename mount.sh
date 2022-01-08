#!/bin/bash
# rename xxx to the right partition
# rename debian to the right user


echo lsblk --fs
echo mkdir ~/SD
echo sudo chown debian ~/SD/
echo sudo mount -t ext4 /dev/xxxp2 ~/SD/
