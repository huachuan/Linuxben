#!/bin/bash
cdir=~/Linuxben/sched_ben
for num in 1 2 3 
do
	mkdir logs
	for sets in fprr bitmap  rbtree
	do	
		for thds in 2 4 8 16 32 64 128 256 512 1024
		do	
			cd ${cdir}
			./linux_ben $sets $thds
			cd ${cdir}/logs
			python ../parse.py $sets$thds.log > $sets$thds.data
			cat ${sets}$thds.data | tr -d 'a-z' >| $thds.data
		done
		paste -d: ${sets}2.data 4.data 8.data 32.data 64.data 128.data 256.data 512.data 1024.data >> output$num.data
	done
	cd ${cdir}
	mv logs logs$num
done

