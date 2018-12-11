#!/usr/bin/env python

# 	Hello friends, comrades, and other folks: I made this software to help randomly generate story cards from Jessica Abel and Matt Madden's book "Drawing Words & Writing Pictures"
#	>  if you want to add new bits, just expand the text files included
#	>  I created this program because it's not always easy to cary the Story Card index cards around.  Inspired by Jessica Abel and Sarah Von Bargen's discussion of creative habits, and the idea of needing "a bookmark habit".  So while i prefer to mostly work on paper, it's nice to have this option on the road!
#
# 	> I'm sure people can make this application slicker and less complicated.

					###### Stuff we'll need to use this application
import random		# We'll need to make random numbers
import datetime		# We'll need to access the computer's clock and calendar
import os			# need to do some file handling stuffs
import shutil		# more o/s stuff I don't understand, I'm an artist, five days a week...

# Adding a bunch of FUNCTIONS.  I'm sure there's a better way of doing this, but, I know zero (0) about programming.  I learned to do this from W3Schools.

def name_change(reader):						#####
													#
	named = reader + '.txt'							# gather the text sent to the function and make it a text file name to reference to lists to pull from.
	occupations = open(named, 'r').readlines()		# open the file with the reference list
	occuno = random.randint(1, len(occupations)-1)	# gather a random item from the first item in the list until the length of the file minus one line
	OccupationForDisplay = occupations[occuno][:-1]	# set the value of the item and remove the end of line data for the value
													#
	return OccupationForDisplay						#### return the value of the randomly selected item


def make_list(num_chars):		 
	"""
	And this little function is here to make the random decisions.
	Fetch the time and date for naming the file and creates a time stamped file for output

	Args:
		num_chars (int): number of characters to be generated
	"""
																																																										 
	now = datetime.datetime.today().strftime('%Y-%m-%d_%H%M%S')																																											
	thisfile = 'Story Spark created [' + str(now) + ']'
 	with open(thisfile + '.txt','a+') as f:
 		f.write("\n######################## NEW STORY CARD ############################### \n \n \n \n** Your Characters ** \n \n")																									
		for x in range (1, num_chars+1):																																																		
 			f.write(str(x) + '. ' + name_change("occupations").upper() + " who is " + name_change("persontraits").upper() + " and [is/has] " + name_change("physicaltraits").upper() + '\n \n')								
 		f.write( "\n** Story Spark **\n\n" + name_change("storysparks").upper() + "\n\nCreative Brainstorm Created On: " + str(now) + "\n###################################################################### \n\n")				
	display_text(thisfile)																																																			
	shutil.move(thisfile + ".txt", "Sessions/" + thisfile + ".txt")																																										
																																																													
										
def display_text(filename):			
	"""
	Args:
        filename (string): name of file to be opened and read
	"""
										# Most of the display in this application is from text files, so this function reads those files and opens them on the screen
	f = open(filename + '.txt', 'r')	# Take the name of 'thisfile' and add '.txt' to the end so it accesses the text file, for read purposes only
	print f.read()						# Print the contents of the file to screen.
	f.close()							# Close the file that was opened.
										
def get_user_input():		
	"""
		returns:
			num_chars (int): Number of characters user wants to generate
	"""																
																								# Allows the user to set the number of characters they want
	while True:																					# While  the data isn't valid...
		try:																					# attempt to...
			num_chars = int(raw_input("? >>> How many characters would you like to include? "))			# capture the number of character as integer 
		except ValueError:																		# but the data isn't an integer
			print("! >>> Sorry, I didn't understand that.  Please input a number")				# prompt an error and instruct for proper data
			continue																			# continue back to data collection
		if num_chars < 0:																				# if the input is integer but less than zero
			print("! >>> Sorry, your response must not be negative.  How do you expect to have fewer than zero characters?!")	# prompt a harassing error and 
			continue																			# continue back to data collection
		else:																					# otherwise, if the data is okay as an integer...
			break																				# escape this validation loop
	return num_chars																					# and send back the number of characters	


def main():
	# checks to see if sessions directory exists in current directory, if not -- create one
	# uses os instead of pathlib for python 2 compatibility
	try: 
		os.makedirs('./sessions')
	except OSError:
		if not os.path.isdir('./sessions'):
			raise

	display_text('opening')	
	num_chars = get_user_input()		
	make_list(num_chars)	


if __name__ == '__main__':
	main()