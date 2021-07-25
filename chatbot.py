#Project: Create your own chatbot
#Step 1 Create a new file. File, Save As, Chatbot.py
#You will make a chatbot that focuses on introducing coding integers in math as well as studying dog breeds in science.
#Step 2 Add code for the introduction
#Pseudocode introduction:
#Print introduction to the chatbot
#Get name from user
#Print hello name
print('Hello. I am Chippy. I am a learnbot.')
print('I will help you learn about dog breeds.')
name = input('What is your name?:')
print('Hello', name , '; it is great to have you as a learning partner!')
#Step 3 Show that you your chatbot can do math
#Pseudocode math
#Get current year from user
#Get learnbot known number of dog species from user
#Print guess is correct
#Convert learnbot known number of dog species to integer
#Set years to 100 - learnbot age
#Print There will be 100 in years
#Convert current year to integer
#Print That will be current year + years
#get year information
year=input('Time for dog breed math. What is the year?:')
print('Yes, that is correct. Thanks for not entering the number of dog days of summer!')
#ask user to guess dog breeds
dogbreeds=input('Can you guess the number of official known dog breeds as of this year? - enter a number that is an integer (for example, 10): ')
print('No, good guess though! I also thought there was this amount: ', dogbreeds)
print('Can you help me find the correct answer on this website?(https://www.hillspet.com/dog-care/behavior-appearance/how-many-dog-breeds-are-there).')
#do math to calculate the number of dog breeds in 100 years
dogbreeds = int(dogbreeds)
nyears = 100 - dogbreeds
print('In 100 years there will be', nyears, 'more dog breeds; research to see if this is true. https://www.sciencefocus.com/nature/are-any-dog-breeds-close-to-becoming-a-new-species/')
print('That will be the year', int(year) +  nyears)
#Challenge: Figure out a way to scrape the hillspet website for the official known number of dog breeds (360). 
#Try this tutorial https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website/
#Here is the code for going to a specific website:
#import webbrowser
#webbrowser.open ("https://www.hillspet.com/dog-care/behavior-appearance/how-many-dog-breeds-are-there")
#Step 4 Start using stored data
#dog breed conversation
print('By the way, I love sheep dogs, also known as Border Collies')
dog = input('How about you? What is your favorite dog?:')
print('I like a', dog, 'too.')
question = 'How many times per week do you train your ' + dog + ' to do new tricks? Enter an integer (for example, 2). '
howoften = input(question)
print('That is interesting. I should do the same with my dog.')
#dog show conversation
dogshow = input('My favorite dog show is The National Dog Show. What is your favorite dog show?')
print(dogshow, '! I like the National Dog Show because it has a category for herding; my dog Lassie herds the chickens in every night.')
print('I wonder if the', dogshow, 'has good dog treats for a', dog,'?')
#Step 5 Add Feelings
feeling = input('You have done well with your lesson so far; how are you feeling today (if you are not sure what today is, check out the line below)?:')
#Type code for accessing today's date, resource: https://www.programiz.com/python-programming/datetime/current-datetime
from datetime import date
today = date.today()
#Complete code for feelings
print("Today's date:", today)
print('Why are you feeling', feeling, 'now?')
reason = input('Please tell me:')
print('I understand. Thanks for sharing!')
#Step 6 Goodbye
#emoji coding resource: https://medium.com/analytics-vidhya/how-to-print-emojis-using-python-2e4f93443f7e
print('Goodbye,', name,';it was fun learning with you!')
print("I hope you will choose me as your learnbot tomorrow", "\N{winking face}")
print('Hasta la proxima . . . Until next time.')