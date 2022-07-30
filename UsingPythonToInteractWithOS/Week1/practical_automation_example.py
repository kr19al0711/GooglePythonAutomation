#!/usr/bin/env python3

import shutil
import psutil 

path = 'E:/'
du = shutil.disk_usage(path)
print(du)
disk_usage_percentage = (du.free/du.total) * 100
print("Free Disk Percentage : {}%".format(disk_usage_percentage))

print("Average CPU usage over 5 seconds : {}%".format(psutil.cpu_percent(5)))
