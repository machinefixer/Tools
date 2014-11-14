#!/usr/bin/env python
import os, sys

filePostfix  = sys.argv[1]
rootDir      = sys.argv[2]
countFiles   = 0

for dirpath, subFolders, files in os.walk(rootDir):
	for f in files:
		if f.split('.')[-1] == filePostfix:
			os.remove(os.path.join(dirpath, f))
			print "file %s has been removed." % f
			countFiles += 1

print "Total Removed: %d Files." % countFiles

			

			
