import cv2
import numpy as np
import math
import os
import sys

# Get distance between two points and floor it
def distance_int(x1, y1, x2, y2):
	return int(math.sqrt(((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1))))

def process_image(directory,path):
	# Read in sample image
	#im = cv2.imread('base_images/D13_032173_1031_XN_76S227W.tiff')
	print('Working on ' + path)
	print('Test')
	im = cv2.imread(directory+'/'+path)
	# Apply border to image, otherwise contour doesn't work
	image=cv2.copyMakeBorder(im, top=10, bottom=10, left=10, right=10, borderType= cv2.BORDER_CONSTANT, value=[0,0,0] )
	image2=cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
	print('Image2')
	del im
	# Seperate the black background pixels and the rest using threshold
	ret,thresh = cv2.threshold(image2,0,255,cv2.THRESH_BINARY)
	print('Thresh')
	del ret
	del image2

	# Find edges (don't know if needed)
	#edges = cv2.Canny(thresh,100,300,apertureSize = 3)
	#print(' Found edges')

	# Get all contours
	contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	print('Contours')
	del hierarchy
	del thresh
	#del edges

	# Find the largest contour (which is the one we want)
	final_contour = contours[0]
	area = 0
	for cnt in contours:
		hull = cv2.convexHull(cnt)
		simplified_cnt = cv2.approxPolyDP(hull,0.001*cv2.arcLength(hull,True),True)
		rect = cv2.boundingRect(simplified_cnt)
		x, y, w, h = rect
		if w*h > area:
			final_contour=cnt
			area=w*h
		del hull
		del simplified_cnt
		del rect

	x1=99999999
	y1=99999999
	x2=-1
	y2=99999999
	x3=-1
	y3=99999999
	x4=99999999
	y4=-1
	for i in range(0, len(final_contour)):
		point=final_contour[i]
		if point[0][0] < x1: # topleft
			x1=point[0][0]
			y1=point[0][1]
		elif point[0][0] == x1:
			if point[0][1] < y1:
				x1=point[0][0]
				y1=point[0][1]
		if point[0][1] < y2: #topright
			x2=point[0][0]
			y2=point[0][1]
		elif point[0][0] == y2:
			if point[0][0] > x2:
				x2=point[0][0]
				y2=point[0][1]
		if point[0][0] > x3: #bottomright
			x3=point[0][0]
			y3=point[0][1]
		elif point[0][0] == x3:
			if point[0][1] < y3:
				x3=point[0][0]
				y3=point[0][1]
		if point[0][1] > y4: #bottomleft
			x4=point[0][0]
			y4=point[0][1]
		elif point[0][0] == y4:
			if point[0][0] < x4:
				x4=point[0][0]
				y4=point[0][1]

	print('Coords')
	del contours
	x1=int(x1)
	y1=int(y1)
	x2=int(x2)
	y2=int(y2)
	x3=int(x3)
	y3=int(y3)
	x4=int(x4)
	y4=int(y4)
	four_points = np.asarray([[[x1,y1]],[[x2,y2]],[[x3,y3]],[[x4,y4]]])
	width=min(distance_int(x1,y1,x2,y2),distance_int(x4,y4,x3,y3))
	height=min(distance_int(x4,y4,x1,y1),distance_int(x3,y3,x2,y2))
	image_points = np.asarray([[[0,0]],[[width,0]],[[width,height]],[[0,height]]])


	# Trasform
	(H,mask) = cv2.findHomography(four_points.astype('single'),image_points.astype('single'))
	print('Find homography')
	#final_image = cv2.warpPerspective(image,H,(width, height))

	# Write output image
	#cv2.imwrite(path,final_image)
	cv2.imwrite(path,cv2.warpPerspective(image,H,(width, height)))
	print('Image write')
	#cv2.drawContours(image, [four_points], -1, (0,255,0), 3)
	#cv2.imwrite('contour2.tiff',image)
	del H
	del mask
	del image

def main():
	if sys.argc >= 2:
		directory=sys.argv[1]
		files = [f for f in os.listdir(directory) if os.path.isfile(f)]
		for path in files:
			process_image(directory+'/',path)
	else:
		files = [f for f in os.listdir('.') if os.path.isfile(f)]
		for path in files:
			process_image('',path)

if __name__ == '__main__':
	#main()
	process_image('base_images','P13_006229_0951_XN_84S014W.tiff')
	print('Finished')




#print(right_contour)
#for i in range(mini,len(final_contour)):
#	sorted_contour.append(final_contour[i])
#for i in range(0,mini):
#	sorted_contour.append(final_contour[i])


#sorted_contour = np.asarray(sorted_contour)

#x1=0
#y1=0
#x2=sorted_contour[0][0][0]
#y2=sorted_contour[0][0][1]
#rec=[[[0,0]]]
#prev='none'
#right=False
#left=False
#up=False
#down=False
#new_w=0
#new_h=0
#print(sorted_contour)
#for i in range(1,len(sorted_contour)):
#	x3=sorted_contour[i][0][0]
#	y3=sorted_contour[i][0][1]
#	if x3-x2 > 0 and y3-y2 <= 0:
#		# right
#		if prev=='none':
#			prev='right'
#			right=True
#		else:
#			dis=distance_int(x2,y2,x3,y3)
#			x1+=dis
#			if x1 < 0:
#				x1=0
#			if y1 < 0:
#				y1 = 0
#			new_w=max(new_w,x1)
#			if prev != 'right':
#				if right:
#					print('Error, did right twice')
#				else:
#					prev='right'
#					right=True
#	elif x3-x2 < 0 and y3-y2 >= 0:
#		# left
#		if prev=='none':
#			prev='left'
#			left=True
#		else:
#			dis=distance_int(x2,y2,x3,y3)
#			x1-=dis
#			if x1 < 0:
#				x1=0
#			if y1 < 0:
#				y1 = 0
#			new_w=max(new_w,x1)
#			if prev != 'right':
#				if right:
#					print('Error, did right twice')
#				else:
#					prev='right'
#					right=True
#	elif y3-y2 > 0 and x3-x2 >= 0:
#		# down
#	elif y3-y2 < 0 and x3-x2 <= 0:
#		# up
#	else:
#		print('Erorr mapping points')
#	x2=x3
#	y2=y3

	
	

#print(hull)
#print(simplified_cnt)

#(H,mask) = cv2.findHomography(final_contour.astype('single'),np.array([[[0., 0.]],[[2150., 0.]],[[2150., 2800.]],[[0.,2800.]]],dtype=np.single))
#width, height = cv2.GetSize(image)
#height, width = image.shape[:2]
#print(str(height) + "," + str(width))
#(H,mask) = cv2.findHomography(final_contour.astype('single'),np.array([[[0., 0.]],[[width, 0.]],[[width, height]],[[0.,height]]],dtype=np.single))
#(H,mask) = cv2.findHomography(final_contour.astype('single'),final_contour.astype('single'))

#final_image = cv2.warpPerspective(image,H,(2150, 2800))

#cv2.imwrite('final.tiff',final_image)

#final_image.show()


