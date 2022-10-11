import shutil
import psutil

# diskUsage = shutil.disk_usage("/")
# print(diskUsage)
# percentage of free disk space
#print(diskUsage.free/diskUsage.total * 100)

# CPU
# print(psutil.cpu_percent(0.1))

# PRACTICAL AUTOMATION EXAMPLE


def check_disk_usage(disk):
    diskUsage = shutil.disk_usage(disk)
    free = diskUsage.free/diskUsage.total * 100
    return free > 20


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75


if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everything is OK !")
