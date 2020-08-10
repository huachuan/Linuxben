import os
import sys
import numpy as np

file = str(sys.argv[1])
rb_res = []
bm_res = []
fprr_res = []
temp = 0
tail = 0

with open(file, "r") as f:
    for line in f:
        if line.startswith("rbtree:"):
            temp = int(line.split()[1].strip())
            rb_res.append(temp)
#           temp = int(line.split()[2].strip())
#           rb_io.append(temp)
        if line.startswith("bitmap:"):
            temp = int(line.split()[1].strip())
            bm_res.append(temp)
#           temp = int(line.split()[2].strip())
#           bm_io.append(temp)
        if line.startswith("fprr:"):
            temp = int(line.split()[1].strip())
            fprr_res.append(temp)
#           temp = int(line.split()[2].strip())
#           fprr_io.append(temp)

tail = int(1000*0.99)

if len(rb_res) > 0:
     print "rbtree res len:{}".format(len(rb_res))
     print "rbtree remove mean:{}".format(np.mean(rb_res))
#    print "rbtree insert mean:{}".format(np.mean(rb_io))
     print "rbtree remove std:{}".format(np.std(rb_res, ddof=1))
#    print "rbtree insert std:{}".format(np.std(rb_io, ddof=1))
     rb_res.sort()
#    rb_io.sort()
     print "rbtree 99% remove overhead:{}".format(rb_res[tail])
#    print "rbtree 99% insert overhead:{}".format(rb_io[tail])
     print "-----------------------------------"

if len(bm_res) > 0:
     print "bitmap res len:{}".format(len(bm_res))
     print "bitmap remove mean:{}".format(np.mean(bm_res))
#    print "bitmap insert mean:{}".format(np.mean(bm_io))
     print "bitmap remove std:{}".format(np.std(bm_res, ddof=1))
#    print "bitmap insert std:{}".format(np.std(bm_io, ddof=1))
     bm_res.sort()
#    bm_io.sort()
     print "bitmap 99% remove overhead:{}".format(bm_res[tail])
#    print "bitmap 99% insert overhead:{}".format(bm_io[tail])
     print "-----------------------------------"

if len(fprr_res) > 0:
     print "fprr res len:{}".format(len(fprr_res))
     print "fprr remove mean:{}".format(np.mean(fprr_res))
#    print "fprr insert mean:{}".format(np.mean(fprr_io))
     print "fprr remove std:{}".format(np.std(fprr_res, ddof=1))
#    print "fprr insert std:{}".format(np.std(fprr_io, ddof=1))
     fprr_res.sort()
#    fprr_io.sort()
     print "fprr 99% remove overhead:{}".format(fprr_res[tail])
#    print "fprr 99% insert overhead:{}".format(fprr_io[tail])
     print "-----------------------------------"

