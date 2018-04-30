import csv
import sys
import shutil

def gold(csv_file, src, dst):
	csvfile=open(csv_file, 'rb') # CSV File name that contains subjectid, CTX Image, x y offset
	done=0
	_swiss=0
	_spiders=0
	_bspiders=0
	_craters=0
	_channels=0
	_none=0
	lastsubjectid=''
	csvreader = csv.DictReader(csvfile, delimiter=',')
	for row in csvreader:
		done+=1
		subjectid = row['subject_id']
		response=row['response']
		if subjectid == lastsubjectid:
			continue
		else:
			if response == '[Craters]':
				_craters += 1
				shutil.copy2(src+'/'+subjectid+'.png',dst+'/craters')
			elif response == '[Channel Network]':
				_channels += 1
				shutil.copy2(src+'/'+subjectid+'.png',dst+'/channels')
			elif response == '[Baby Spiders]':
				_bspiders += 1
				shutil.copy2(src+'/'+subjectid+'.png',dst+'/bspiders')
			elif response == '[Swiss Cheese Terrain]':
				_swiss += 1
				shutil.copy2(src+'/'+subjectid+'.png',dst+'/swiss')
			elif response == '[Spiders]':
				_spiders += 1
				shutil.copy2(src+'/'+subjectid+'.png',dst+'/spiders')
			elif response == '[None of the Above Features Are Present]':
				_none += 1
				shutil.copy2(src+'/'+subjectid+'.png',dst+'/none')
			else:
				print('\n' + subjectid + ' : ' + response)
			sys.stdout.write("\r%d subjects done." % (done))
			sys.stdout.flush()
			lastsubjectid=subjectid
	print('\nSpiders=' + str(_spiders))
	print('Swiss='+ str(_swiss))
	print('Baby Spiders='+ str(_bspiders))
	print('Channel Network='+ str(_channels))
	print('Craters='+ str(_craters))
	print('None=' + str(_none))




if __name__ == "__main__":
	if len(sys.argv) < 4:
		print('Please use format CSV_File, Subject_Source_directory, Subject_Category_Destination_Directory')
		sys.exit(-1)
	gold(sys.argv[1], sys.argv[2], sys.argv[3])



