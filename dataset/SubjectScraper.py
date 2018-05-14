import csv
import sys
import urllib
import cStringIO
import time
from selenium import webdriver # external download

def main():
	url = "https://www.zooniverse.org/projects/mschwamb/planet-four-terrains/classify"
	browser = webdriver.Firefox() # This won't work if you don't download selenium webdriver
	browser.get(url)
	innerHTML = browser.execute_script("return document.body.innerHTML").encode('utf-8')
	browser.quit()

	# Get CSV Filename from args
	csvfile=open('spider_swiss_scores.csv', 'rb')

	# Read in all lines from CSV file (seperated by comma)
	csvreader = csv.DictReader(csvfile, delimiter=',')
	# For each row in CSV file
	for row in csvreader:
		subject=row['subject_id']
		if subject in innerHTML:
			print('Bang!')

	print('Finished')

	#f=open("subject.txt","w+")
	#f.write(innerHTML)
	#f.close()

if __name__=='__main__':
	main()
