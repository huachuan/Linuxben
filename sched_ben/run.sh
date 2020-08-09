#!/bin/bash
cdir=~/Linuxben/sched_ben
for num in 1 2 3 4 5
do
	mkdir logs
	for sets in fprr bitmap  rbtree
	do	
		for thds in 64 128 256 512 1023
		do	
			cd ${cdir}
			./linux_ben $sets $thds
			cd ${cdir}/logs
			python ../parse.py $sets$thds.log > $sets$thds.data
			cat ${sets}$thds.data | tr -d 'a-z' >| $thds.data
		done
		paste -d: ${sets}64.data 128.data 256.data 512.data 1023.data >> output$num.data
	done
	cd ${cdir}
	mv logs logs$num
done

