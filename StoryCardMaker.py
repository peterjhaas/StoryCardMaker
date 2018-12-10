#!/usr/bin/env python

# 	Hello friends, comrades, and other folks: I made this software to help randomly generate story cards from Jessica Abel and Matt Madden's book "Drawing Words & Writing Pictures"
#	>  if you want to add new bits, just expand the text files included
#	>  I created this program because it's not always easy to cary the Story Card index cards around.  Inspired by Jessica Abel and Sarah Von Bargen's discussion of creative habits, and the idea of needing "a bookmark habit".  So while i prefer to mostly work on paper, it's nice to have this option on the road!
#
# 	> !!! MAKE SURE THAT YOU HAVE A FOLDER CALLED 'SESSIONS' IN THE SAME DIRECTORY AS THE STORYCARD.PY FILE SO THE APPLICATION CAN EXPORT THE RESULTS CORRECTLY. 
# 	> I'm sure people can make this application slicker and less complicated.
#
#	
#
#	>>>>>>>>>>>>>>> ######
					###### Stuff we'll need to use this application
import random		# We'll need to make random numbers
import datetime		# We'll need to access the computer's clock and calendar
import os			# need to do some file handling stuffs
import shutil		# more o/s stuff I don't understand, I'm an artist, five days a week...
					###### Some universal declarations
y = 3				# set to one so the application runs
reader = ""			# Builds the variable for the text file to be read
					######
# <<<<<<<<<<<<<<<<< ######

# Adding a bunch of FUNCTIONS.  I'm sure there's a better way of doing this, but, I know zero (0) about programming.  I learned to do this from W3Schools.

def func_namechange(reader):						#####
													#
	named = reader + '.txt'							# gather the text sent to the function and make it a text file name to reference to lists to pull from.
	occupations = open(named, 'r').readlines()		# open the file with the reference list
	occuno = random.randint(1, len(occupations)-1)	# gather a random item from the first item in the list until the length of the file minus one line
	OccupationForDisplay = occupations[occuno][:-1]	# set the value of the item and remove the end of line data for the value
													#
	return OccupationForDisplay						#### return the value of the randomly selected item


def func_makethelist():		############################################################################################################################################################################################################# And this little function is here to make the random decisions.
																																																										# 
	now = datetime.datetime.today().strftime('%Y-%m-%d_%H%M%S')																																											# Fetch the time and date for naming the file and creates a time stamped file for output
	thisfile = 'Story Spark created [' + str(now) + ']'  																																												# creates a temporary working file																						 
 	with open(thisfile + '.txt','a+') as f:																																																# Create a new text file with the date stamp included in the file name
 		f.write("\n######################## NEW STORY CARD ############################### \n \n \n \n** Your Characters ** \n \n")																										# Add some formating to the file
 		for x in range (1, y+1):																																																		# loop character generation for the number of characters the user wants to create 
 			f.write(str(x) + '. ' + func_namechange("occupations").upper() + " who is " + func_namechange("persontraits").upper() + " and [is/has] " + func_namechange("physicaltraits").upper() + '\n \n')								# write random bits to file
 		f.write( "\n** Story Spark **\n\n" + func_namechange("storysparks").upper() + "\n\nCreative Brainstorm Created On: " + str(now) + "\n###################################################################### \n\n")				# write some formating to file
	func_disptext(thisfile)																																																				# Ask the function disptext to open and display the results of random characters and story spark ####
	shutil.move(thisfile + ".txt", "Sessions/" + thisfile + ".txt")																																										# Tell the OS to move the output file to the Sessions Folder so they stay organized! 
																																																										#
	return					#############################################################################################################################################################################################################
								
										
def func_disptext(thisfile):			###### data input: variable string 'thisfile' 	
										# Most of the display in this application is from text files, so this function reads those files and opens them on the screen
	f = open(thisfile + '.txt', 'r')	# Take the name of 'thisfile' and add '.txt' to the end so it accesses the text file, for read purposes only
	print f.read()						# Print the contents of the file to screen.
	f.close()							# Close the file that was opened.
										#
	return								###### Exit the function, but don't send any information back.
	


def func_characternumber():																		###### 
																								# Allows the user to set the number of characters they want
	while True:																					# While  the data isn't valid...
		try:																					# attempt to...
			y = int(raw_input("? >>> How many characters would you like to include? "))			# capture the number of character as integer 
		except ValueError:																		# but the data isn't an integer
			print("! >>> Sorry, I didn't understand that.  Please input a number")				# prompt an error and instruct for proper data
			continue																			# continue back to data collection
		if y < 0:																				# if the input is integer but less than zero
			print("! >>> Sorry, your response must not be negative.  How do you expect to have fewer than zero characters?!")	# prompt a harassing error and 
			continue																			# continue back to data collection
		else:																					# otherwise, if the data is okay as an integer...
			break																				# escape this validation loop
	return y																					# and send back the number of characters	



						######### The Program Begins			
func_disptext('opening')	#
y = func_characternumber()		#
func_makethelist()			#
							



