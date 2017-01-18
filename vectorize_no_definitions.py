
"""
Created by Eli Zelle on November 21 2016
"""

inputfile1 ='pos-vec_all_POS.txt'
inputfile2 ='DVD4ef_parsed.txt'
outputfile ='Vectorizing_test.txt'


words = np.array([])
values = np.array([])
with open(inputfile1, "r") as vectors:
	vector_reader = csv.reader(vectors, dialect = 'excel-tab')
for row in vector_reader:
		
	words = np.append(words, row[i-1]) # reads in POS tagged words as strings in to a list.
	

	for i in row[1:]:
		one_vector = []
		temp = float(i)
		one_vector = array.append(temp)   # need to read these columns in as floats. Convert them from strings

		if (i==len(row)): # need to append values if we hit the last value in the row
			values = np.append(values, row[i-1])



vector_dict = {}
for i in range(len(words)):
			vector_dict[words[i]] = vectors[i] # keys are POS tagged words, values are ordered lists of floats

with open(inputfile2, 'r') as text_file:
	text_file_reader = csv.reader(text_file, dialect='excel-tab')

with open(outputfile, 'w') as outfile:
	outfile_writer = csv.writer(outfile, delimiter =',')

for row in data_file_reader:
	line = row[0] # might have some issues here with inspecting each vector
	sentance = []
		for word in line:			
			if word not in dictionary.keys():
				continue
			vector = dictionary[line[word]]
		sentance.append(vector)
		average = np.average(sentance, axis = 1)
	outfile_writer(average)


