import csv
import sys
from PIL import Image

# Eric Wright
# Chop up CTX images into subjects

def getSubjects(csv_file, src, dst):
	Image.MAX_IMAGE_PIXELS = 3000000000

	csvfile=open(csv_file, 'rb') # CSV File name that contains subjectid, CTX Image, x y offset

	openimage = ''
	img = None
	done = 0
	csvreader = csv.DictReader(csvfile, delimiter=',')
	for row in csvreader:
		ctx=row[' Parent CTX_image'] # CTX name of image
		subjectid = row['subject_id']
		x = int(row['CTX center x position'])-400
		y = int(row['CTX center y position'])-300
		if openimage != ctx:
			print('\n'+ctx)
			img = Image.open(src + '/' + ctx + '.tif')
			openimage=ctx
		box=(x,y,x+800,y+600)
		region = img.crop(box)
		region.save(dst + '/' + subjectid + '.png')
		done = done+1
		sys.stdout.write("\r%d subjects done." % (done))
		sys.stdout.flush()



if __name__ == "__main__":
	if len(sys.argv) < 4:
		print('Please use format CSV_File, TIFF_Source_Directory, Subject_Destination_Directory')
		sys.exit(-1)
	getSubjects(sys.argv[1], sys.argv[2], sys.argv[3])

