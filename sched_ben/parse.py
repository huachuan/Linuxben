import os
import sys
import numpy as np

file = str(sys.argv[1])
res = []
ro = []
io = []
t_ro = 0
t_io = 0
tail = 0
test_name = ""

with open(file, "r") as f:
    for line in f:
        if not(line.startswith("bitmap:") or line.startswith("fprr:") or line.startswith("rbtree:")):
            continue
        test_name = line.split()[0].strip()
        t_ro = int(line.split()[1].strip())
        ro.append(t_ro)
        t_io = int(line.split()[2].strip())
        io.append(t_io)
        res.append(t_io+t_ro)
        flag = 0

if len(res) < 1000:
	print "ERROR"
	sys.exit(1)

tail = int(len(res)*0.99)

print "{} res len:{}".format(test_name, len(res))
print "{} s_overhead mean:{}".format(test_name, np.mean(res))
print "{} s_overhead std:{}".format(test_name, np.std(res, ddof=1))
res.sort()
io.sort()
ro.sort()
print "{} 99% remove overhead:{}".format(test_name, ro[tail])
print "{} 99% insert overhead:{}".format(test_name, io[tail])
print "{} 99% s_overhead overhead:{}".format(test_name, res[tail])
print "-----------------------------------"
