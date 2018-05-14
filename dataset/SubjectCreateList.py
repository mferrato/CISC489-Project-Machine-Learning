import csv
import sys

def spiderswiss(csv_file):
	csvfile=open(csv_file, 'rb') # CSV File name that contains subjectid, CTX Image, x y offset
	csvreader = csv.DictReader(csvfile, delimiter=',')
	f = open("list.txt", "w+")
	for row in csvreader:
		subjectid = row['subject_id']
		swiss  = float(row['swiss score'])
		spider = float(row['spider score'])
		if swiss > 0.5 and spider > 0.5:
			# For now, ignore it if both match.
			continue
		elif swiss > 0.5:
			f.write('swiss/' + subjectid+'.png\n')
		elif spider > 0.5:
			f.write('spiders/' + subjectid+'.png\n')
		else:
			f.write('none/' + subjectid+'.png\n')
	print('Done')


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print('Please use format CSV_File')
		sys.exit(-1)
	spiderswiss(sys.argv[1])



