import sys

def accuracy(html):

	content = ''
	with open(html, 'r') as content_file:
	    content = content_file.read()

	correct = ''
	incorrect = ''
	numcorrect = 0
	numincorrect = 0
	swisscorrect = 0
	swissincorrect = 0
	nonecorrect = 0
	noneincorrect = 0
	spiderscorrect = 0
	spidersincorrect = 0
	index = content.find('<tr>', content.find('</tr>'))
	end_index = content.find('</tr>',index)
	while(index > 0 and end_index > 0):
		#subject_index = 
		subjectandclass=content[content.find('subject_cat/', index)+12 : content.find('.png', index)]
		subject = subjectandclass[subjectandclass.find('/')+1:]
		terrain = subjectandclass[:subjectandclass.find('/')]
		swiss_index = content.find('"badge">',content.find('swiss',index))+8
		swiss = float(content[swiss_index:content.find('%',swiss_index)])
		none_index = content.find('"badge">',content.find('none',index))+8
		none = float(content[none_index:content.find('%',none_index)])
		spiders_index = content.find('"badge">',content.find('spiders',index))+8
		spiders = float(content[spiders_index:content.find('%',spiders_index)])

		prediction = ''
		if swiss == max(swiss, none, spiders):
			prediction = 'swiss'
		elif none == max(swiss, none, spiders):
			prediction = 'none'
		else:
			prediction = 'spiders'

		if prediction != terrain:
			numincorrect += 1
			incorrect += subject + ": Terrain=" + terrain + " Prediction=" + prediction + "\n"
			if terrain == 'swiss':
				swissincorrect += 1
			elif terrain == 'none':
				noneincorrect += 1
			elif terrain == 'spiders':
				spidersincorrect += 1
		else:
			numcorrect += 1
			correct += subject + ': Terrain=' + terrain + "\n"
			if terrain == 'swiss':
				swisscorrect += 1
			elif terrain == 'none':
				nonecorrect += 1
			elif terrain == 'spiders':
				spiderscorrect += 1

		index = content.find('<tr>', end_index)
		end_index = content.find('</tr>', index)

	with open(html[:html.find('.html')]+'.results', 'w+') as output_file:
		output_string = ''
		output_string += html + '\n'
		output_string += 'Accuracy = '
		output_string += ('%.2f' % ((float(numcorrect)/(numcorrect+numincorrect))*100)) + '%\n'
		output_string += 'Swiss Accuracy = '
		output_string += ('%.2f' % ((float(swisscorrect)/(swisscorrect+swissincorrect))*100)) + '%\n'
		output_string += 'None Accuracy = '
		output_string += ('%.2f' % ((float(nonecorrect)/(nonecorrect+noneincorrect))*100)) + '%\n'
		output_string += 'Spiders Accuracy = '
		output_string += ('%.2f' % ((float(spiderscorrect)/(spiderscorrect+spidersincorrect))*100)) + '%\n'

		print(output_string)
		output_file.write(output_string)
		output_file.write('\n\nOutput Incorrect\n')
		output_file.write(incorrect)
		output_file.write('\n\nOutput Correct\n')
		output_file.write(correct)

if __name__ == "__main__":
	accuracy(sys.argv[1])
	print('Done!')










