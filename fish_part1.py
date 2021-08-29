# pseudocode for fish conservation app (code for part 1 shown, part 2 to follow next week)
# import math and use dictionary module for possessionLimit, maxFishLength and fishTally
# use math.inf to indicate no limit for a species or a fish length
# define maxFishLength and fishTally
# if elif else lines of code to tell the user what to do if their fish catch does / does not qualify

print('For Keeps!') 
print('++++++++++++++++++++++')
print('Find out the kind, length and amount of Massachusetts saltwater fish you can catch.')
print('This is a starter list and will help you become aware of fish conservation efforts.')
print('~~~~~~~~~~~~~~~~~~~~~~')
print('What is at the end of your line? Take a look at the limits before you determine if you can keep your fish.')

possessionLimit = {
		"Acadian Redfish" : math.inf,
		"Winter Flounder" : 8
	}

#What is the maximum length of the fish?
#Use the dictionary module {}
maxFishLength = {
		"Acadian Redfish" : math.inf,
		"Winter Flounder" : 12
	}
fishTally = {
		"Acadian Redfish" : 0,
		"Winter Flounder" : 0
	}

