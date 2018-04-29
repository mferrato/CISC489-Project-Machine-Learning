from pysis.isis import mroctx2isis, spiceinit, ctxcal, isis2std
import os
import sys
import csv

# func('CTX Image with name (no extension)', 'source directory', 'directory to save to')
def process_ctx(ctx, src, dst):
	IMG = src+'/'+ctx+'.IMG'
	CUB = ctx+'.cub'
	CALCUB = ctx+'.cal.cub'
	TIFF = dst+'/'+ctx+'.tif' # Directory must already exist!

	mroctx2isis(from_=IMG, to=CUB)
	spiceinit(from_=CUB)
	ctxcal(from_=CUB, to=CALCUB)
	isis2std(from_=CALCUB, to=TIFF, format_='TIFF')

	os.remove(CUB)
	os.remove(CALCUB)


if __name__ == "__main__":
	if len(sys.argv) < 4:
		print('CSV File, CTX_Source_Directory, and TIFF_Destination Directory as command line arguments.')
		sys.exit(-1)
	src=sys.argv[2]
	dst=sys.argv[3]
	csvfile=open(sys.argv[1], 'rb')

	csvreader = csv.DictReader(csvfile, delimiter=',')
	for row in csvreader:
		ctx=row['CTX image'] # CTX name of image
		print(ctx)
		process_ctx(ctx, src, dst)


