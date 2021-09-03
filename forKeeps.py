# pseudocode for fish conservation app 
# import math module and use dictionary module for possessionLimit, maxFishLength and fishTally
# import webbrowser for fish species identification
# use math.inf to indicate no limit for a species or a fish length (there is no possession limit on the Acadian Redfish)
# define maxFishLength and fishTally
# use if, elif, else lines of code to tell the user what to do if their fish catch does / does not qualify
# e to exit app

import math 

#Use Google Image Search and NOAA for fish identification
print('For Keeps!') 
print('++++++++++++++++++++++')
print('Find out the kind, amount and length of Massachusetts saltwater fish you can catch.')
print('This is not an exhaustive list, but this will help you become aware of fish conservation efforts.')
print('~~~~~~~~~~~~~~~~~~~~~~')
print('What is at the end of your line?') 
print('~~~~~~~~~~~~~~~~~~~~~~')
print('If you are not sure of the species, upload a picture to Google Image Search or go to the NOAA Fisheries website.')
print ('Note: Two new browser tabs will open')

# Wait three to four seconds; both websites will open
print('Note: Google Image - click on the camera icon, then upload an image of the fish you caught.')
print('~~~~~~~~~~~~~~~~~~~~~~')
import webbrowser
webbrowser.open_new_tab('https://www.google.com/imghp')

#Use the NOAA Fisheries website
import webbrowser
webbrowser.open_new_tab('https://www.fisheries.noaa.gov/species/winter-flounder')

#Fish limits overview
print ('Take a look at the limits before you determine if you can keep your fish.')
print ('Note: inf = no limits')
print('~~~~~~~~~~~~~~~~~~~~~~')

#How many of a certain fish species can you catch?
#Use the dictionary module {}
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
#This will keep a running tally and possession limit of each fish species you catch
fishTally = {
		"Acadian Redfish" : 0,
		"Winter Flounder" : 0
	}
gameOver = False
while not gameOver:
    print("possession limits")
    print(possessionLimit)
    print("This is the number of fish you have caught")
    print(fishTally)
    print("maximum length allowed for fish")
    print(maxFishLength)

# Insert the input of fish length in inches
    fishLength = input ('How long is the fish you caught (inches)?: ') 

# Add the fish species
    print('Alewife (a), Acadian Redfish (ar), Windowpane Flounder (wf) (or e to exit):')
    item = input('Can I keep the fish? Type the one or two-letter code to find out: ')
    if item == 'e':
        gameOver = True
    elif item == 'a':

# Notification if the fish species is illegal to catch
        print("You are going to have to throw this one back. Try Again.")
    elif item =='ar':
        print('You can keep this fish!')

# Run the app two or three times to see the tally change next to each fish species
        fishTally['Acadian Redfish']+=1
    elif item == 'wf':
        print('Your fish is ', fishLength, ' long')
        if fishTally['Winter Flounder'] < possessionLimit["Winter Flounder"]:

# Use the float() method to compare the Winter Flounder maximum length of twelve inches
            if float(fishLength) <= maxFishLength['Winter Flounder']:
                print() 
                print('You can keep this fish!')
                fishTally['Winter Flounder'] +=1
            else:
                print('You have the incorrect fish length')
                
        else:
            print('You have caught your limit')
    print()