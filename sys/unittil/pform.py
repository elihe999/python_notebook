import psutil

mem = psutil.virtual_memory()
print(mem.total, "  ", mem.used)
print(mem.free)
#swap
print("swap: ", psutil.swap_memory())
print("cpu time:  ", psutil.cpu_times())
print("cpu count: ", psutil.cpu_count())

#disk
print("disk", psutil.disk_partitions())
print("used / ", psutil.disk_usage('/'))
print("io :", psutil.disk_io_counters())
print("io :", psutil.disk_io_counters(perdisk=True))

#net
print("net io: ", psutil.net_io_counters())
print("net io: ", psutil.net_io_counters(pernic=True))

print("user: ", psutil.users())


