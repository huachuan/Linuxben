#!/bin/bash
cdir=~/Linuxben/sched_ben
for num in 1 2 3 4 5
do
	mkdir logs
	for sets in fprr bitmap  rbtree
	do	
		for thds in 10 100 1000
		do	
			cd ${cdir}
			./linux_ben $sets $thds
			cd ${cdir}/logs
			python ../parse.py $sets$thds.log > $sets$thds.data
			cat ${sets}$thds.data | tr -d 'a-z' >| $thds.data
		done
		paste -d: ${sets}10.data 100.data 1000.data >> output$num.data
	done
	cd ${cdir}
	mv logs logs$num
done

