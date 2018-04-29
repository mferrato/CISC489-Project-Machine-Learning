import csv
import sys
import urllib
import cStringIO
import time
from selenium import webdriver # external download
from pysis.isis import edrget # This is the built in tool for the image download, but it doesn't work for me :)
import os

# CTXScraper2.py
# Eric Wright, Mauricio Ferrato

# Uses ISIS edrget application to download CTX IMG files.
# Need to run these files through CTXProcess before we can begin working on them.

def getIMG(ctx):
	mrox=getMROX(ctx)
	ctxurl='http://pdsimg.jpl.nasa.gov/data/mro/mars_reconnaissance_orbiter/ctx/'+mrox+'/data/'+ctx+'.IMG'
	# Download IMG
	retry=True # Error handling in case of network error
	while(retry):
		try:
			urllib.urlretrieve(ctxurl, ctx+".IMG", reporthook=downloadtime)
			retry=False
		except (KeyboardInterrupt, SystemExit):
			raise
		except Exception as e:
			print('\n'+str(e))
			retry=True
			print('Connection error.. Retrying')
	print('') #newline



# In order to get the correct URL, we must first get the MROX information.
def getMROX(ctx):
	url = "https://viewer.mars.asu.edu/viewer/ctx#P=" + ctx + "&T=2" # Database URL based on CTX

	# Need to load inner HTML code, can only be accessed after webpage fully loads up
	# Need to open a browser to allow webpage to load file completely
	browser = webdriver.Firefox() # This won't work if you don't download selenium webdriver
	browser.get(url)
	innerHTML = browser.execute_script("return document.body.innerHTML").encode('utf-8')

	# Find MROX
	mroxLoc = innerHTML.find('mrox')
	while mroxLoc==-1:  # Error handling, sometimes the page doesn't
		            # fully load before trying to grab inner HTML

		innerHTML = browser.execute_script("return document.body.innerHTML").encode('utf-8')
		mroxLoc = innerHTML.find('mrox')

	browser.quit()
	return innerHTML[mroxLoc:mroxLoc+9]


# Function for printing the progress of the IMG download
def downloadtime(count, block_size, total_size):
	global start_time
	if count == 0:
		start_time = time.time()
		return
	duration = time.time() - start_time
	progress_size = int(count * block_size)
	speed = int(progress_size / (1024 * duration))
	#percent = int(count * block_size * 100 / total_size)
	percent = min(int(count*block_size*100/total_size),100)
	sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" % (percent, progress_size / (1024 * 1024), speed, duration))
	sys.stdout.flush()




if __name__ == "__main__":
	# Get CSV Filename from args
	csvfile=open(sys.argv[1], 'rb')
	directory=sys.argv[2]

	# Read in all lines from CSV file (seperated by comma)
	csvreader = csv.DictReader(csvfile, delimiter=',')
	# For each row in CSV file
	for row in csvreader:
		ctx=row['CTX image'] # CTX name of image
		print(ctx)
		getIMG(ctx)
		os.rename(ctx+'.IMG', directory+'/'+ctx+'.IMG')
	print('Finished')

