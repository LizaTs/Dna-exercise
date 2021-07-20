import csv

def data(csvfile): 
# Opens the information stored in database as a list of dictionaries
	path = 'C:/Users/Soffi/Desktop/liza/dna/databases/' + csvfile
	with open(path) as file:
		database = csv.DictReader(file)
		return list(database)

def sequence(file):
# Opens files to be matched to database
	path ='C:/Users/Soffi/Desktop/liza/dna/sequences/' +  file
	with open(path) as raw_seq:
		seq = raw_seq.read()
	return seq

###############################################################################################################
if __name__ == '__main__':
	# Empy (for now) variables
	seqs_count = {}
	people = [] # Contains dictionaries of info about people inside the database
	per_vals = [] # Same as people, in the form of list
	names = [] # Kinda unzips per_vals. creates list of names of people inside the database
	vals = [] # Creates list of the count of dna sequences of people inside the database

	# Read files
	database = data(input('plaese enter database: '))# Calls "data" function and creates small database
	seq = sequence(input('please enter file name: ')) # Calls "sequence" function and makes data usable

	# Count sequences
	dna = dict(database[1]).keys()
	dna = list(dna)
	dna = dna[1:]

	for dat in dna:
		index = 0
		r_count = 0 # The real, final count of sequences
		t_count = 0 # A temporary count of sequences. Becomes r_count when sequence is longest
		while index < len(seq):
			if seq[index:index + len(dat)] == dat:
				t_count = t_count + 1
				index = index + len(dat)
			else:
				if t_count > r_count:
					r_count = t_count
				t_count = 0
				index = index + 1
		seqs_count[dat] = str(r_count)

	##########################################################################################################
	# Match sequences

	suspect = list(seqs_count.values()) # Contains info of each "suspect"

	for person in database: # Creates dictionaries with info of each person inside the database
		people.append(person.values())

	#match lists
	for person in people:
		person = list(person)
		names.append(person[0])
		vals.append(person[1:])

	for person in vals:
		if suspect in vals:
			criminal = vals.index(suspect)
			print(names[criminal])
		else:
			print("no match")
		break