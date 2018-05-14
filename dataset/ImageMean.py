import cv2
import numpy as np
import sys
import csv
from os import walk
#import matplotlib.pyplot as plt
from scipy.stats import itemfreq

BLACK=0
WHITE=255
GRAY=127
OFFSET=0.2

def whiteblack(i, mean):
	if i > mean*(1.0-OFFSET) and i < mean*(1.0+OFFSET):
		return WHITE
	else:
		return i
	#if mean > GRAY: # really light image
	#	if i < mean*(1.0-OFFSET): # Very dark
	#		return BLACK
	#	elif i > mean*(1.0+OFFSET): # Very light
	#		return GRAY
	#	else: # Average
	#		return WHITE
	#else: # reall dark image
	#	if i < mean*(1.0-OFFSET): # Very dark
	#		return GRAY
	#	elif i > mean*(1.0+OFFSET): # Very light
	#		return BLACK
	#	else: # Average
	#		return WHITE

def whiteblacksubject(subjectid, src, dst):
	print(src+'/'+subjectid + '->' + dst+'/'+subjectid)
	img = cv2.imread(src+'/'+subjectid+'.png', cv2.IMREAD_GRAYSCALE)
	average_color = np.mean(img)

	for row in range(len(img)):
	    for col in range(len(img[row])):
		img[row][col] = whiteblack(img[row][col],average_color)
	cv2.imwrite(dst+'/'+subjectid+'.png',img)

def processcsv(csv_file, src, dst):
	done = 0
	csvfile=open(csv_file, 'rb') 
	csvreader = csv.DictReader(csvfile, delimiter=',')
	for row in csvreader:
		subjectid = row['subject_id']
		whiteblacksubject(subjectid, src, dst)
		done+=1
		sys.stdout.write("\r%d subjects done." % (done))
		sys.stdout.flush()
	print('\nDone')

def processdir(src, dst):
	done=0
	for (dirpath, dirnames, filenames) in walk(src):
		for f in filenames:
			whiteblacksubject(f[:-4], dirpath, dst+'/'+dirpath[len(src)+1:])
			done+=1
			sys.stdout.write("\r%d subjects done." % (done))
			sys.stdout.flush()
	print('\nDone')
		

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print('Please use format CSV_File, Subject_Source_Directory, Subject_Destination_Directory')
		sys.exit(-1)
	elif len(sys.argv) < 4:
		processdir(sys.argv[1], sys.argv[2])
	else:
		processcsv(sys.argv[1], sys.argv[2], sys.argv[3])


#img = cv2.imread('subjects/1040425.png',cv2.IMREAD_GRAYSCALE)

#average_color = np.mean(img)

#print(average_color)

#for row in range(len(img)):
#    for col in range(len(img[row])):
#        img[row][col] = whiteblack(img[row][col],average_color)

#cv2.imwrite('test.png',img)

#vf = np.vectorize(whiteblack)




#def array_for(x):
#    return np.array([f(xi) for xi in x])

#>>> g = numpy.vectorize(lambda x: x + 5)
#>>> %timeit g(a)
