import csv
import sys
import shutil

def spiderswiss(csv_file, src, dst):
	csvfile=open(csv_file, 'rb') # CSV File name that contains subjectid, CTX Image, x y offset
	done=0
	spider_count=0
	swiss_count=0
	none_count=0
	csvreader = csv.DictReader(csvfile, delimiter=',')
	for row in csvreader:
		subjectid = row['subject_id']
		swiss  = float(row['swiss score'])
		spider = float(row['spider score'])
		if swiss > 0.5 and spider > 0.5:
			# For now, ignore it if both match.
			done+=1
			continue
		elif swiss > 0.5:
			shutil.copy2(src+'/'+subjectid+'.png',dst+'/swiss')
			done+=1
			swiss_count+=1
		elif spider > 0.5:
			shutil.copy2(src+'/'+subjectid+'.png',dst+'/spiders')
			done+=1
			spider_count+=1
		else:
			shutil.copy2(src+'/'+subjectid+'.png',dst+'/none')
			done+=1
			none_count+=1
		sys.stdout.write("\r%d subjects done." % (done))
		sys.stdout.flush()
	print('\nSpiders=' + str(spider_count))
	print('Swiss='+ str(swiss_count))
	print('None=' + str(none_count))


if __name__ == "__main__":
	if len(sys.argv) < 4:
		print('Please use format CSV_File, Subject_Source_directory, Subject_Category_Destination_Directory')
		sys.exit(-1)
	spiderswiss(sys.argv[1], sys.argv[2], sys.argv[3])



