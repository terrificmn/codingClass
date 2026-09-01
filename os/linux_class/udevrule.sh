#!/bin/bash

kennel="1-1.4"
vendor="0403"
product="6001"
symlink_name="ttyGps"
filename="98-gps.rules"
dir_file_name="/etc/udev/rules.d/"

echo ""
echo "This script copies gps udev rules to /etc/udev/rules.d/"
echo ""

echo "ublox Gps (USB Serial from -) : /dev/ttyUSBx to /dev/ttyGps :"
if [ -f "/etc/udev/rules.d/98-gps.rules" ]; then
    echo "$filename file already exist."
else
    echo 'SUBSYSTEM=="tty", KERNELS=="'$kennel'", ATTRS{idVendor}=="'$vendor'", ATTRS{idProduct}=="'$product'", MODE:="0666", GROUP:="dialout", SYMLINK+="'$symlink_name'"' > $dir_file_name$filename
    echo "$filename created"
fi

echo ""
echo "Reload rules"
echo ""
sudo udevadm control --reload-rules
sudo udevadm trigger
