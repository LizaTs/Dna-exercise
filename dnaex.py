import csv
# Keep a space and capitalization between the hash sign and the comment i.e.
#read files vs/
# Read files
# Don't be scared to give them their own line

def data(csvfile): # Opens the information stored in database as a list of dictionaries
	# The path is still not realtive so your code basically won't run on any machine except yours
	path ='C:/Users/liza-and-soffi/Desktop/liza/DNA/databases/' + csvfile
	with open(path) as file:
		database = csv.DictReader(file)
		return list(database)

def sequence(file): # Opens files to be matched to database
	path = 'C:/Users/liza-and-soffi/Desktop/liza/DNA/sequences/' + file # Same here this is bad
	with open(path) as raw_seq:
		seq = raw_seq.read()
	return seq

# Line delimiters are cool but you should just double line it
###################################################################################################################
if __name__ == '__main__':
	# Empy (for now) variables
	seqs_count = []
	people = [] # Contains dictionaries of info about people inside the database
	per_vals = [] # Same as people, in the form of list
	names = [] # Kinda unzips per_vals. creates list of names of people inside the database
	vals = [] # Creates list of the count of dna sequences of people inside the database

	# Read files
	# TODO implement with argv as a Command Line Application
	database = data(input('plaese enter database: ')) # Calls "data" function and creates small database
	seq = sequence(input('please enter file name: ')) # Calls "sequence" function and makes data usable

	# Count sequences
	dna = list(database[1:])

	for dat in dna:
		index = 0
		r_count = 0 # Real, final count of sequences
		t_count = 0 # Temporary count, becomes r_count when sequence is longest
		while index < len(seq):
			if seq[index:index + len(dat)] == dat:
				t_count = t_count + 1
				index = index + len(dat)
			else:
				if t_count > r_count:
					r_count = t_count
				t_count = 0
				index = index + 1
		seqs_count.append(r_count)

# Match sequences
	suspect = list(seqs_count.values()) # Contains info of each "suspect"

	for line in database: # Creates dictionaries with info of each person inside the database
		person = dict(line)
		people.append(person)
	# Read the database as a dict convert to list just do make it a dictionary again??

	for person in people: # Converts data inside dictinaries into lists
		person = person.values()
		per_vals.append(list(person))

# If you pick a line delimiter you should make it consistent
#__________________________________________

# Match lists

	for person in per_vals:
		names.append(person[0])
		vals.append(person[1:])

	for person in vals:
		if suspect in vals:
			criminal = vals.index(suspect)
			print(names[criminal])
		else:
			print("no match")
		break