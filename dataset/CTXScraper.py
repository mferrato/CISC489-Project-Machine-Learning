import csv
import sys
import urllib
import cStringIO
import time
from selenium import webdriver # external download

# CTXScraper.py
# Eric Wright, Mauricio Ferrato

# Used to download CTX images from https://viewer.mars.asu.edu/viewer/ctx
# These images are TIFF format, which is the highest quality image we can get

# Takes as input the name of a CSV file
# This file should have a column named "CTX image" that contains the CTX image name


def main():
	# Get CSV Filename from args
	csvfile=open(sys.argv[1], 'rb')

	# Read in all lines from CSV file (seperated by comma)
	csvreader = csv.DictReader(csvfile, delimiter=',')
	# For each row in CSV file
	for row in csvreader:
		ctx=row['CTX image'] # CTX name of image
		print(ctx)
		url = "https://viewer.mars.asu.edu/viewer/ctx#P=" + ctx + "&T=2" # Database URL based on CTX

		# Need to load inner HTML code, can only be accessed after webpage fully loads up
		# Need to open a browser to allow webpage to load file completely
		browser = webdriver.Firefox() # This won't work if you don't download selenium webdriver
		browser.get(url)
		innerHTML = browser.execute_script("return document.body.innerHTML").encode('utf-8')

		# TIFF URL under "Pyramidized TIFF"
		pyLoc = innerHTML.find('Pyramidized TIFF')
		bLoc = innerHTML.rfind('href=', 0, pyLoc)
		eLoc = innerHTML.rfind('" target="_blank">', 0, pyLoc)
		while(pyLoc==-1 or bLoc==-1 or eLoc==-1): # Error handling, sometimes the page doesn't
			print("Failed.. retrying")        # fully load before trying to grab inner HTML
			browser.quit()
			browser = webdriver.Firefox()
			browser.get(url)
			innerHTML = browser.execute_script("return document.body.innerHTML").encode('utf-8')
			pyLoc = innerHTML.find('Pyramidized TIFF')
			bLoc = innerHTML.rfind('href=', 0, pyLoc)
			eLoc = innerHTML.rfind('" target="_blank">', 0, pyLoc)

		# TIFF URL
		tiffurl = innerHTML[bLoc+6:eLoc]
		print(tiffurl)
		browser.quit()

		# Download TIFF
		retry=True # Error handling in case of network error
		while(retry):
			try:
				urllib.urlretrieve(tiffurl, ctx+".tiff", reporthook=downloadtime)
				retry=False
			except (KeyboardInterrupt, SystemExit):
				raise
			except Exception as e:
				print('\n'+str(e))
				retry=True
				print('Connection error.. Retrying')
		print('\n' + ctx + ' finished.')

	csvfile.close()


# Function for printing the progress of the TIFF download
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



if __name__=='__main__':
	main()


# END SCRIPT




# Everything after this point is from us trying to figure it out/testing stuff

#html = urllib2.urlopen("https://viewer.mars.asu.edu/viewer/ctx#P=D13_032173_1031_XN_76S227W&T=2")

#soup = BeautifulSoup(html, "html.parser")

#texts=soup.findAll(text=True)

#urlfile=open("url.txt", "w+")
#urlfile.write(u" ".join(t.strip() for t in texts))
#urlfile.close()

#for img_link in soup.findAll('a'):
#	print img_link.get('href')

#browser = webdriver.Firefox()
#url = "https://viewer.mars.asu.edu/viewer/ctx#P=D13_032173_1031_XN_76S227W&T=2"
#      "https://viewer.mars.asu.edu/viewer/ctx#P=D14_032510_0963_XN_83S054W&T=3"
#browser.get(url)
#innerHTML = browser.execute_script("return document.body.innerHTML").encode('utf-8')

#urlfile=open("url.txt", "w+")
#urlfile.write(innerHTML)
#urlfile.close()

#browser = webdriver.Firefox()
#url = "https://viewer.mars.asu.edu/viewer/ctx#P=D13_032298_0969_XN_83S028W&T=2"
#browser.get(url)
#print(url)
#innerHTML = browser.execute_script("return document.body.innerHTML").encode('utf-8')
#innerHTML = browser.execute_script("return document.body.innerHTML")
#urlfile=open("url.txt", "w+")
#urlfile.write(innerHTML)
#urlfile.close()
#print(innerHTML)
#locMrox = innerHTML.find("mrox_")
#print(locMrox)
#mrox = innerHTML[locMrox:locMrox+9]
#print(mrox)
#urllib.urlretrieve("https://image.mars.asu.edu/stream/"+ctx+".tiff?image=/mars/images/ctx/"+mrox+"/prj_full/"+ctx+".tiff", ctx+".tiff")
#print(row['CTX image'])
#browser.quit()

	

#https://image.mars.asu.edu/stream/D14_032574_0969_XN_83S005W.tiff?image=/mars/images/ctx/mrox_1853/prj_full/D14_032574_0969_XN_83S005W.tiff
#https://image.mars.asu.edu/stream/D13_032173_1031_XN_76S227W.tiff?image=/mars/images/ctx/mrox_1839/prj_full/D13_032173_1031_XN_76S227W.tiff


